<p align="center">
  <a href="https://walkccc.github.io/LeetCode/"><img src="https://i.imgur.com/mDXzzNp.png" width="300" title="LeetCode" alt="LeetCode"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/-1470/2152%20=%2068.31%25%20Solved-blue.svg?style=flat-square" />
  <img src="https://img.shields.io/badge/-Easy%20327-5CB85D.svg?style=flat-square" />
  <img src="https://img.shields.io/badge/-Medium%20812-F0AE4E.svg?style=flat-square" />
  <img src="https://img.shields.io/badge/-Hard%20331-D95450.svg?style=flat-square" />
</p>

# LeetCode Solutions

## Getting Started

This repository contains C++, Java, and Python solutions to [LeetCode](https://leetcode.com/problemset/all/).

Also, I build a website by [GitHub Actions](https://github.com/features/actions) to host the code files by Markdown files.
You can see the built page here: [LeetCode Solutions](https://walkccc.github.io/LeetCode/).

## Coding Style

> I believe messy code is costing you.
>
> Therefore, I follow the formatter 99% of the time, but in rare situations, I format the code manually because it might look better in these cases.
>
> Saving vertical rows and trying to squeeze everything in a single line disrespects the column limit and makes the code hard to read.
>
> This repository aims to provide code with good readability and consistent style over various topics and embraces new standards. In most situations, readability has more value than lines of code and tiny performance hop.

- **C++** code is formatted by [clang-format](https://clang.llvm.org/docs/ClangFormat.html) following the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html#Spaces_vs._Tabs). You can see the configuration [here](https://github.com/google/leveldb/blob/master/.clang-format).
- **Java** code is formatted by [clang-format](https://clang.llvm.org/docs/ClangFormat.html) following the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html).
- **Python** code is formatted by [autopep8](https://pypi.org/project/autopep8/) following [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) except passing the argument `--indent-size=2` for a better viewing experience in mobile devices.

Take a look at my nvim configuration related to auto formatting.

In `~/.config/nvim/init.lua`:

```lua
local LUA_DIR = '$HOME/.config/nvim/lua/'

local function sourceLuaFiles(subpath)
  local p = io.popen('ls ' .. LUA_DIR .. subpath .. '| grep .lua')
  for filename in p:lines() do
    local fsPath = subpath .. filename
    local requirePath = fsPath:gsub('%.lua', ''):gsub('/', '.')
    require(requirePath)
  end
end

sourceLuaFiles('')
sourceLuaFiles('plugins/')
```

In `~/.config/nvim/lua/plugins.lua`:

```lua
-- Use packer plugin
local status_ok, packer = pcall(require, 'packer')
if not status_ok then return end

-- Install your plugins here
return packer.startup(function(use)
  -- Null LS
  use 'jose-elias-alvarez/null-ls.nvim' -- for formatters and linters
end)
```

In `~/.config/nvim/lua/plugins/null-ls.lua`:

```lua
local status_ok, null_ls = pcall(require, "null-ls")
if not status_ok then
  return
end

local formatting = null_ls.builtins.formatting

null_ls.setup {
  debug = false,
  sources = {
    formatting.autopep8.with { extra_args = { '--indent-size=2' } },
    formatting.clang_format,
  },
  on_attach = function(client)
    if client.resolved_capabilities.document_formatting then
      -- Format on save
      vim.cmd([[
      augroup LspFormatting
        autocmd! * <buffer>
        autocmd BufWritePre <buffer> lua vim.lsp.buf.formatting_sync()
      augroup END
      ]])
    end
  end,
}
```

## More Information

The repository is still under construction, and the goal is to keep up with the growth of LeetCode problems by the end of the year!

For more information, please visit my [**GitHub**](https://github.com/walkccc/).

Hosted the site on Feb 23, 2019.

Revised on Dec 25, 2019.

Added `init.vim` on Jan 18, 2021.

Updated to `init.lua` on Jan 1, 2022.
