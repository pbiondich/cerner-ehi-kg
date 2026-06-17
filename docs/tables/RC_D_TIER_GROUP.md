# RC_D_TIER_GROUP

> Contains tiers that charges have the ability to post to.

**Description:** Revenue Cycle Dimension Tier Group  
**Table type:** REFERENCE  
**Primary key:** `RC_D_TIER_GROUP_ID`  
**Columns:** 13  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 5 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 6 | `MILL_TIER_GROUP_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the related tier group code in the Millennium database. |
| 7 | `RC_D_TIER_GROUP_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies tiers that charges have the ability to post to. |
| 8 | `TIER_GROUP_NAME` | VARCHAR(40) | NOT NULL |  | The name of the tier to which the charge has the ability to post. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (7)

| From table | Column |
|------------|--------|
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_TIER_GROUP_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_TIER_GROUP_ID` |
| [RC_F_DLY_CHRG_ASSOC_SMRY](RC_F_DLY_CHRG_ASSOC_SMRY.md) | `RC_D_TIER_GROUP_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_TIER_GROUP_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_TIER_GROUP_ID` |
| [RC_F_MTH_CHRG_ASSOC_SMRY](RC_F_MTH_CHRG_ASSOC_SMRY.md) | `RC_D_TIER_GROUP_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_TIER_GROUP_ID` |

