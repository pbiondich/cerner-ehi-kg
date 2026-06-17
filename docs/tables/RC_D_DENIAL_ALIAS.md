# RC_D_DENIAL_ALIAS

> This table contains denial alias information such as denial type and denial group.

**Description:** Revenue Cycle Dimension Denial Alias  
**Table type:** ACTIVITY  
**Primary key:** `RC_D_DENIAL_ALIAS_ID`  
**Columns:** 17  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DENIAL_ALIAS_REASON` | VARCHAR(40) | NOT NULL |  | Contains the alias associated with a denial. |
| 4 | `DENIAL_CODE` | VARCHAR(50) | NOT NULL |  | The actual denial code sent on an ERA. |
| 5 | `DENIAL_GROUP` | VARCHAR(40) | NOT NULL |  | The group associated with a denial code (i.e. Patient Liability, Information Only). |
| 6 | `DENIAL_TYPE` | VARCHAR(40) | NOT NULL |  | The based type of the denial. (Provider, Patient, Technical, Information Only). |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 10 | `MILL_DENIAL_REASON_CD` | DOUBLE | NOT NULL |  | Represent the denial reason for a particular denial. |
| 11 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 12 | `RC_D_DENIAL_ALIAS_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies denial alias information such as denial type and denial group. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [RC_F_DAILY_DENIAL_SMRY](RC_F_DAILY_DENIAL_SMRY.md) | `RC_D_DENIAL_ALIAS_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_D_DENIAL_ALIAS_ID` |
| [RC_F_MONTHLY_DENIAL_SMRY](RC_F_MONTHLY_DENIAL_SMRY.md) | `RC_D_DENIAL_ALIAS_ID` |
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_DENIAL_ALIAS_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_DENIAL_ALIAS_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_DENIAL_ALIAS_ID` |

