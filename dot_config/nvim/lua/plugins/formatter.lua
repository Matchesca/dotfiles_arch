return {
    'stevearc/conform.nvim',
    event = { "BufWritePre" }, -- Run formatters before saving
    cmd = { "ConformInfo" },
    opts = {
        -- Define your formatters here
        formatters_by_ft = {
            -- Use the 'prettier' formatter for these filetypes
            javascript = { "prettier" },
            typescript = { "prettier" },
            javascriptreact = { "prettier" },
            typescriptreact = { "prettier" },
            vue = { "prettier" },
            css = { "prettier" },
            scss = { "prettier" },
            less = { "prettier" },
            html = { "prettier" },
            json = { "prettier" },
            yaml = { "prettier" },
            markdown = { "prettier" },
            graphql = { "prettier" },
            -- Use 'gofmt' or 'goimports' for Go
            go = { "goimports" },       -- or "gofmt"
            -- Use 'ruff_format' or 'black' for Python
            python = { "ruff_format" }, -- or "black" or "isort", "black"
            -- Use 'stylua' for Lua
            lua = { "stylua" },
        },

        -- Optional: Set up format-on-save
        format_on_save = {
            -- Disable formatting on save for languages that shouldn't be auto-formatted
            -- Other languages will be formatted on save based on formatters_by_ft
            lsp_fallback = true, -- Try LSP formatting if no conform formatter is found
            timeout_ms = 500,    -- Stop formatting if it takes too long
        },

        -- Optional: Customize formatter options
        -- formatters = {
        --   prettier = {
        --     -- By default, conform searches for config files (.prettierrc, etc.)
        --     -- You can override arguments if needed:
        --     -- args = {"--print-width", "100"}
        --   },
        --   stylua = {
        --     -- args = {"--config-path", vim.fn.stdpath("config") .. "/stylua.toml"}
        --   }
        -- }
    },
    init = function()
        -- Optional: Add a format command or keymap
        -- vim.api.nvim_create_user_command("Format", function(args)
        --   require("conform").format({ async = true, lsp_fallback = true, range = args.range })
        -- end, { range = true })
        vim.keymap.set({ "n", "v" }, "<leader>lf", function()
            require("conform").format({ async = true, lsp_fallback = true })
        end, { desc = "Format buffer with Conform" })
    end,
}
