# PM_FLX_REG_RULE

> Contains information on the restrictions placed on PM_FLX_TASK as to what types of conversations specific applications can invoke.

**Description:** Person Management Flexible Registration Rule.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_APP_NUM` | DOUBLE |  |  | The ending number for the range of applications a rule applies to. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PRODUCT_ID` | DOUBLE |  |  | This is the unique identifier from the product table of the product associated with the registration rule. |
| 7 | `RULE` | VARCHAR(25) |  |  | Text that signals what type of rule/restriction applies.. |
| 8 | `RULE_ID` | DOUBLE | NOT NULL |  | Unique identifier for the rule. |
| 9 | `START_APP_NUM` | DOUBLE |  |  | The starting number for the range of applications a rule applies to. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALUE` | VARCHAR(25) |  |  | Rule/Restrction value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

