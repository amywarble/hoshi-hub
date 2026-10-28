# Preview Hoshi Hub locally

On Windows, install Ruby 3.3 using Chocolatey from an elevated PowerShell:

```powershell
choco install ruby.install --version=3.3.13.1 -y
```

This uses the same Ruby series as the toolchain used to verify this site's
GitHub Pages dependencies. Package details are on
[Chocolatey's Ruby page](https://community.chocolatey.org/packages/ruby.install).

Open a new **PowerShell terminal as administrator** so Ruby is on PATH, then
install its development tools. The MSYS2 installer cannot request elevation
itself when launched from the command line:

```powershell
ridk.cmd install
```

The `.cmd` extension selects the batch launcher, so this also works when
PowerShell's execution policy blocks `ridk.ps1`.

Press Enter to select the default components `[1,3]`: the MSYS2 base installation
and MINGW development toolchain. The
development tools build native dependencies used by Jekyll. Alternatively,
install **Ruby+Devkit 3.3.x (x64)** from
[RubyInstaller](https://rubyinstaller.org/downloads/) and complete the same
`ridk.cmd install` step. See the
[Jekyll Windows installation guide](https://jekyllrb.com/docs/installation/windows/).

Once this finishes, close the administrator terminal. In a normal PowerShell
terminal, install Bundler, then let it install the site dependencies:

```powershell
gem install bundler
Set-Location C:\Users\amylh\Desktop\git\pocket-kgs-support
bundle install
bundle exec jekyll serve --livereload --force_polling
```

Open <http://127.0.0.1:4000/hoshi-hub/>. Leave the terminal running while editing;
Jekyll rebuilds changed pages and LiveReload refreshes the browser. Stop the
server with Ctrl+C. Restart it after changing `_config.yml`.

The Gemfile installs the Jekyll version and plugins used by GitHub Pages, so a
separate global Jekyll installation is unnecessary. Re-run `bundle install` when
the Gemfile changes. The first setup and remote-theme download require internet
access. Local preview does not upload or publish anything to GitHub.

Optional checks before publishing (requires Python 3):

```powershell
python scripts/check-translations.py
bundle exec jekyll build --strict_front_matter
python scripts/check-translations.py --site _site
```

For background, see
[GitHub's local Jekyll preview guide](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).
