# AAC → CEL Mapping Examples

## Example 1: Check for High Risk Users

AAC:
  if (context.getRiskScore() > 75) { denyAccess(); }
CEL:
  user.risk > 75

## Example 2: Time-Based Restriction

AAC:
  var hour = context.getHourOfDay();
  if (hour < 8 || hour > 18) stepUp();
CEL:
  outside_business_hours(time.hour)

## Example 3: Geo Restriction

AAC:
  if (country not in allowedCountries) { requireMFA(); }
CEL:
  is_unusual_country(user.geoCountry, ["US", "CA", "UK"])

## Example 4: Device Binding Check

AAC:
  if (!device.isBound()) requireMFA();
CEL:
  device.isBound == false