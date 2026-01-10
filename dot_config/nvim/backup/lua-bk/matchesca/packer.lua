

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'

  use {
	  'nvim-telescope/telescope.nvim', tag = '0.1.8',
	  -- or                            , branch = '0.1.x',
	  requires = { {'nvim-lua/plenary.nvim'} }
  }
  use({ 'rose-pine/neovim', as = 'rose-pine' })
  use{"folke/tokyonight.nvim",
       opts = {},
   }
  vim.cmd.colorscheme('tokyonight')

  use('nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'})
  use('nvim-treesitter/playground')
  use('theprimeagen/harpoon')
--  use {
--	  "windwp/nvim-autopairs",
--	  event = "InsertEnter",
--	  config = function()
--		  require("nvim-autopairs").setup {}
--	  end
--  }

  use('mbbill/undotree')

-- Status line
  use('vim-airline/vim-airline')

  use('tpope/vim-fugitive')
  use {
  'VonHeikemen/lsp-zero.nvim',
  branch = 'v3.x',
  requires = {
    --- Uncomment the two plugins below if you want to manage the language servers from neovim
    {'williamboman/mason.nvim'},
    {'williamboman/mason-lspconfig.nvim'},

    {'neovim/nvim-lspconfig'},
    {'hrsh7th/nvim-cmp'},
    {'hrsh7th/cmp-nvim-lsp'},
    {'L3MON4D3/LuaSnip'},
    {'rafamadriz/friendly-snippets'},

    -- Autocompletion
    {'hrsh7th/cmp-path'},
    {'hrsh7th/cmp-buffer'},
    }
    }
   use('windwp/nvim-ts-autotag')
   use('jose-elias-alvarez/null-ls.nvim')
   use('MunifTanjim/prettier.nvim')
   use {
    'goolord/alpha-nvim',
    }

    -- Leetcode
    use{
        "kawre/leetcode.nvim",
        build = ":TSUpdate html",
        requires = {
            "nvim-telescope/telescope.nvim",
            "nvim-lua/plenary.nvim", -- required by telescope
            "MunifTanjim/nui.nvim",
            "nvim-tree/nvim-web-devicons",
            "rcarriga/nvim-notify",
},
        config = function ()
            require('leetcode').setup()
        end
}

    -- Latex stuff
    use({'lervag/vimtex',
        config = function ()
            vim.g.vimtex_view_method = "skim"
            vim.g.maplocalleader = "\\"
            vim.g.vimtex_view_skim_sync = 1
            vim.g.vimtex_view_skim_activate = 1
    end})

    -- Github copilot stuff
    use('github/copilot.vim')
end)
