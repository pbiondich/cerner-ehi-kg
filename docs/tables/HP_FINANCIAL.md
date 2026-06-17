# HP_FINANCIAL

> Stores financial data for plans, benefits, and procedure benefits for a plan.

**Description:** To Be Dropped in Rev 7.9  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COINSURANCE` | DOUBLE |  |  | Value of coinsurance amount (percent, i.e. 80 percent) |
| 7 | `COPAY` | DOUBLE |  |  | Value of benefits copay amount (in dollars) |
| 8 | `DEDUCTIBLE` | DOUBLE |  |  | Value of benefit s deductible (in dollars) |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the health plan to which this financial information belongs. |
| 11 | `HP_FINANCIAL_ID` | DOUBLE | NOT NULL |  | Unique identifier for this health plan financial record. |
| 12 | `LIFETIME_MAX_BNFT` | DOUBLE |  |  | The lifetime maximum benefit (in dollars) for the related benefit or plan. |
| 13 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Stores location, if financial info varies according to location where benefit is received. |
| 14 | `MAX_FAM_OUT_POCKET` | DOUBLE |  |  | Value, in dollars, representing the max amount that the covered family would be required to pay out of pocket for covered benefits. |
| 15 | `MAX_OUT_POCKET` | DOUBLE |  |  | Value, in dollars, representing the max amount that the covered individual would be required to pay out of pocket for covered benefits. |
| 16 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key to the parent entity table record to which this financial record is related. |
| 17 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | Name of the parent entity table, to which this financial record is related. |
| 18 | `REMARKS` | VARCHAR(200) |  |  | Remarks |
| 19 | `SPECIALTY_CD` | DOUBLE | NOT NULL |  | Used to store the specialty_cd value if this financial record is related to a specialty type benefit. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

