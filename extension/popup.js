const captureView = document.getElementById('capture-view');
const settingsView = document.getElementById('settings-view');
const settingsToggle = document.getElementById('settings-toggle');
const settingsForm = document.getElementById('settings-form');
const cancelSettings = document.getElementById('cancel-settings');
const pageHost = document.getElementById('page-host');
const pageTitle = document.getElementById('page-title');
const pageUrl = document.getElementById('page-url');
const savePageButton = document.getElementById('save-page');
const issueLink = document.getElementById('issue-link');
const statusMessage = document.getElementById('status');

let activePage = null;
let savedSettings = null;

function setStatus(message, state = '') {
  statusMessage.textContent = message;
  statusMessage.dataset.state = state;
}

function showSettings(show) {
  settingsView.hidden = !show;
  captureView.hidden = show;
  settingsToggle.textContent = show ? 'Page' : 'Settings';
  cancelSettings.hidden = !show || !savedSettings;
  setStatus('');
}

function populateSettings(settings) {
  document.getElementById('owner').value = settings?.owner || '';
  document.getElementById('repo').value = settings?.repo || '';
  document.getElementById('token').value = settings?.token || '';
}

async function loadActivePage() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab?.url || !/^https?:\/\//i.test(tab.url)) {
    savePageButton.disabled = true;
    pageHost.textContent = 'Unavailable page';
    pageTitle.value = '';
    pageUrl.textContent = 'Open a regular web page to capture it.';
    return;
  }
  activePage = { url: tab.url, title: tab.title || new URL(tab.url).hostname };
  pageHost.textContent = new URL(tab.url).hostname;
  pageTitle.value = activePage.title;
  pageUrl.textContent = activePage.url;
}

async function initialize() {
  try {
    const settings = await chrome.storage.local.get(['owner', 'repo', 'token']);
    savedSettings = settings.owner && settings.repo && settings.token ? settings : null;
    populateSettings(settings);
    await loadActivePage();
    showSettings(!savedSettings);
    if (savedSettings && !activePage) {
      setStatus('This browser page cannot be saved.', 'error');
    }
  } catch {
    setStatus('Could not read extension settings or active tab.', 'error');
  }
}

settingsToggle.addEventListener('click', () => showSettings(settingsView.hidden));
cancelSettings.addEventListener('click', () => showSettings(false));

settingsForm.addEventListener('submit', async event => {
  event.preventDefault();
  const owner = document.getElementById('owner').value.trim();
  const repo = document.getElementById('repo').value.trim();
  const token = document.getElementById('token').value.trim();
  if (!/^[A-Za-z0-9-]+$/.test(owner) || !/^[A-Za-z0-9_.-]+$/.test(repo) || !token) {
    setStatus('Enter a valid GitHub owner, repository, and token.', 'error');
    return;
  }
  try {
    await chrome.storage.local.set({ owner, repo, token });
    savedSettings = { owner, repo, token };
    showSettings(false);
    setStatus('Settings saved in this browser profile.', 'success');
  } catch {
    setStatus('Could not save extension settings.', 'error');
  }
});

savePageButton.addEventListener('click', async () => {
  if (!savedSettings || !activePage || savePageButton.disabled) return;
  const title = pageTitle.value.trim() || activePage.title || 'New Reference';
  savePageButton.disabled = true;
  issueLink.hidden = true;
  setStatus('Submitting reference...');
  try {
    const endpoint = `https://api.github.com/repos/${encodeURIComponent(savedSettings.owner)}/${encodeURIComponent(savedSettings.repo)}/issues`;
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${savedSettings.token}`,
        Accept: 'application/vnd.github+json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ title, body: activePage.url })
    });
    const result = await response.json().catch(() => ({}));
    if (!response.ok) {
      if (response.status === 401) throw new Error('Token rejected. Check your token and repository access.');
      if (response.status === 403) throw new Error('GitHub denied access. Check Issues: read and write permission and token limits.');
      throw new Error(result.message || `GitHub returned ${response.status}.`);
    }
    setStatus(`Issue #${result.number} submitted. Metadata processing will run automatically.`, 'success');
    issueLink.href = result.html_url;
    issueLink.hidden = false;
  } catch (error) {
    setStatus(error.message || 'Could not submit this page.', 'error');
  } finally {
    savePageButton.disabled = false;
  }
});

initialize();
