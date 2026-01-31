@echo off
cd /d "C:\CDC AI APP BUILDER"

REM Stage all modified and new files
git add index.html cdc_locked_v0_1.html cdc_locked_v0_3.html cdc_locked_v1_1.html cdc_locked_v1_2.html cdc_locked_v1_3.html

REM Commit with clear message
git commit -m "CDC Ai App Builder v1.1–v1.3 Batch Rollout — polishing, commercial, and audit layers consolidated"

REM Push to GitHub
git push origin main

echo.
echo ✅ GitHub update complete: v1.1–v1.3 batch rollout pushed.
pause
