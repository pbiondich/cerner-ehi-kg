# MED_OE_DEFAULTS

> Contains values used as defaults for many attributes of an order.

**Description:** Medical Order Entry Defaults  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 44

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALTERNATE_DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | alternate dispense category |
| 3 | `COMMENT1_ID` | DOUBLE | NOT NULL | FK→ | The LONG_TEXT_ID of the first comment for the product. |
| 4 | `COMMENT1_TYPE` | DOUBLE |  |  | Indicates what the first comment for the product applies to. |
| 5 | `COMMENT2_ID` | DOUBLE | NOT NULL | FK→ | The LONG_TEXT_ID of the second comment for the product. |
| 6 | `COMMENT2_TYPE` | DOUBLE |  |  | Indicates what the second comment for the product applies to. |
| 7 | `CONT_DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The dispense category that will default when the product is ordered with an order type of continuous. |
| 8 | `DAW_CD` | DOUBLE | NOT NULL |  | Dispense options and rules. |
| 9 | `DEFAULT_PAR_DOSES` | DOUBLE |  |  | The number of doses to default when the product is ordered as PRN. |
| 10 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The dispense category that will default when the product is ordered. |
| 11 | `DURATION` | DOUBLE |  |  | The dose that will be defaulted when the default dose (default strength and/or default volume) cannot be parsed into an individual strength and/or volume. |
| 12 | `DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | The frequency that will default when the product is ordered. |
| 13 | `FREETEXT_DOSE` | VARCHAR(255) |  |  | The dose that will be defaulted when the default dose cannot be parsed into an individual strength and/or volume. |
| 14 | `FREETEXT_RATE_TXT` | VARCHAR(100) |  |  | String that represents the rate for an order that cannot be defined with a standard numeric representation. |
| 15 | `FREQUENCY_CD` | DOUBLE | NOT NULL |  | The frequency that will default when the product is ordered. |
| 16 | `GRACE_PERIOD_DAYS` | DOUBLE | NOT NULL |  | The number of days in the grace period defined for a product for Lot Tracking. |
| 17 | `INFUSE_OVER` | DOUBLE |  |  | The amount of time over which the order will be infused that will default when the product is ordered. |
| 18 | `INFUSE_OVER_CD` | DOUBLE | NOT NULL |  | The infuse over unit that will default when the product is ordered. |
| 19 | `INT_DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The dispense category that will default when the product is ordered with an order type of intermittent. |
| 20 | `MAX_PAR_SUPPLY` | DOUBLE |  |  | The maximum number of PRN doses that can be given in a 24 hour period. Display only. |
| 21 | `MED_DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The dispense category that will default when the product is ordered with an order type of medication. |
| 22 | `MED_OE_DEFAULTS_ID` | DOUBLE | NOT NULL |  | Unique, generated number that will identify a single row on the MED_OE_DEFAULTS table. |
| 23 | `NBR_LABELS` | DOUBLE |  |  | The number of label copies that default when the product is dispensed. |
| 24 | `NORMALIZED_RATE_NBR` | DOUBLE | NOT NULL |  | Default volume or strength per weight and/or time rate for the product or set. |
| 25 | `NORMALIZED_RATE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure of the normalized rate. |
| 26 | `ORD_AS_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Text representing the default synonym to which the product will be associated when ordered. |
| 27 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The price schedule that will default when the product is ordered. |
| 28 | `PRN_IND` | DOUBLE |  |  | Indicates whether or not the product will default as PRN when ordered. |
| 29 | `PRN_REASON_CD` | DOUBLE | NOT NULL |  | Indicates the PRN reason that will default when the PRN Indicator is set to default as checked. |
| 30 | `RATE_NBR` | DOUBLE | NOT NULL |  | Default volume per time rate of infusion for the product or set. |
| 31 | `RATE_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for the infusion rate. |
| 32 | `ROUTE_CD` | DOUBLE | NOT NULL |  | The route of administration that will default when the product is ordered. |
| 33 | `RX_QTY` | DOUBLE |  |  | The default initial prescription quantity when the product is ordered. |
| 34 | `SIG_CODES` | VARCHAR(255) |  |  | The sig code that will default when the product is ordered. |
| 35 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | The default stop type that defaults when the product is ordered. |
| 36 | `STRENGTH` | DOUBLE |  |  | The strength that will be defaulted when the default dose can be parsed into an individual strength and/or volume. |
| 37 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | The strength unit that will be defaulted when the default dose can be parsed into an individual strength and/or volume. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `VOLUME` | DOUBLE |  |  | The volume that will be defaulted when the default dose can be parsed into an individual strength and/or volume. |
| 44 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | The volume unit that will be defaulted when the default dose can be parsed into an individual strength and/or volume. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT1_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `COMMENT2_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORD_AS_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

