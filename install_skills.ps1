$ErrorActionPreference = "Continue"
Set-Location "C:\Project\thinking_agent"

$repos = @(
    @{ url = "https://github.com/affaan-m/ECC.git"; target = "external/sources/ecc" },
    @{ url = "https://github.com/anthropics/claude-code.git"; target = "external/sources/anthropic-claude-code" },
    @{ url = "https://github.com/anthropics/claude-code-action.git"; target = "external/sources/anthropic-claude-code-action" },
    @{ url = "https://github.com/anthropics/skills.git"; target = "external/sources/anthropic-skills" },
    @{ url = "https://github.com/anthropics/claude-plugins-official.git"; target = "external/sources/anthropic-claude-plugins-official" },
    @{ url = "https://github.com/openai/codex.git"; target = "external/sources/openai-codex" },
    @{ url = "https://github.com/google-gemini/gemini-cli.git"; target = "external/sources/google-gemini-cli" },
    @{ url = "https://github.com/anomalyco/opencode.git"; target = "external/sources/opencode" },
    @{ url = "https://github.com/modelcontextprotocol/servers.git"; target = "external/sources/modelcontextprotocol-servers" },
    @{ url = "https://github.com/modelcontextprotocol/registry.git"; target = "external/sources/modelcontextprotocol-registry" },
    @{ url = "https://github.com/github/github-mcp-server.git"; target = "external/sources/github-mcp-server" },
    @{ url = "https://github.com/openai/agents.md.git"; target = "external/sources/agents-md" },
    @{ url = "https://github.com/forrestchang/andrej-karpathy-skills.git"; target = "external/sources/andrej-karpathy-skills" },
    @{ url = "https://github.com/mbeijen/andrej-karpathy-skills-cursor-vscode.git"; target = "external/sources/andrej-karpathy-skills-cursor-vscode" },
    @{ url = "https://github.com/thedotmack/claude-mem.git"; target = "external/sources/claude-mem" },
    @{ url = "https://github.com/obra/superpowers.git"; target = "external/sources/superpowers" },
    @{ url = "https://github.com/shanraisshan/claude-code-best-practice.git"; target = "external/sources/claude-code-best-practice" },
    @{ url = "https://github.com/hesreallyhim/awesome-claude-code.git"; target = "external/sources/awesome-claude-code" },
    @{ url = "https://github.com/VoltAgent/awesome-agent-skills.git"; target = "external/sources/awesome-agent-skills" },
    @{ url = "https://github.com/wshobson/agents.git"; target = "external/sources/wshobson-agents" },
    @{ url = "https://github.com/vercel-labs/agent-skills.git"; target = "external/sources/vercel-agent-skills" },
    @{ url = "https://github.com/PatrickJS/awesome-cursorrules.git"; target = "external/sources/awesome-cursorrules" },
    @{ url = "https://github.com/matank001/cursor-security-rules.git"; target = "external/sources/cursor-security-rules" }
)

$total = $repos.Count
$success = 0
$failed = 0

foreach ($repo in $repos) {
    $idx = $repos.IndexOf($repo) + 1
    Write-Host "[$idx/$total] Cloning $($repo.url) -> $($repo.target)" -ForegroundColor Cyan
    
    if (Test-Path $repo.target) {
        Write-Host "  Already exists, skipping." -ForegroundColor Yellow
        $success++
        continue
    }

    git clone --depth 1 $repo.url $repo.target 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  OK" -ForegroundColor Green
        $success++
    } else {
        Write-Host "  FAILED (exit code $LASTEXITCODE)" -ForegroundColor Red
        $failed++
    }
}

Write-Host "`n=== Summary ===" -ForegroundColor White
Write-Host "Total: $total | Success: $success | Failed: $failed" -ForegroundColor White
