---
title: "How to Rejoin a Computer to a Domain"
date: 2026-04-30
categories: [work]
tags: [active-directory, domain-join, windows, sysadmin]
image: /assets/img/domain-join.svg
---

## Overview

When a computer loses its domain trust relationship or requires rejoin to the domain, follow this procedure to properly remove and rejoin the machine.

## Prerequisites

- Local administrator credentials on the target computer
- Domain administrator credentials for rejoining

## Steps

1. Log in using local administrator credentials
2. Remove the computer from the domain by switching to a workgroup (e.g., `WORKGROUP`)
3. Restart the computer to apply changes
4. Log in with local administrator credentials again
5. Join the computer back to the domain using domain administrator credentials
6. Restart when prompted to complete the process

## PowerShell Automation

For those who prefer automation, here's a PowerShell snippet:

```powershell
# Remove from domain
Remove-Computer -UnjoinDomainCredential (Get-Credential) -PassThru -Restart

# After restart, join to domain
Add-Computer -DomainName "yourdomain.com" -Credential (Get-Credential) -Restart
```

## Notes

- Ensure you have domain administrator privileges before attempting to rejoin the computer
- Standard user accounts and local domain accounts cannot perform domain join operations
- Always backup important data before making domain changes
- Consider using PowerShell remoting for bulk operations across multiple machines