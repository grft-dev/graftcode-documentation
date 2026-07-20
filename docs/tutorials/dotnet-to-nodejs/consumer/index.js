"use strict";

const {
  GraftConfig,
  BillingService,
} = require("@graft/nuget-billingservice");

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;

(async () => {
  const total = await BillingService.calculateMonthlyBill(12.5, 4);
  console.log(`Monthly bill: ${total}`);
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
