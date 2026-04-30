---
title: "How to Rejoin a Computer to a Domain"
date: 2026-04-30
categories: [technology]
tags: [active-directory, domain-join, windows, sysadmin]
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

## Notes

Ensure you have domain administrator privileges before attempting to rejoin the computer, as standard user accounts cannot perform domain join operations. Nor can Local Domain Accounts