# DOSE_RANGE_CHECK

> Table is used as a placeholder for content updates and versioning of dose range rules. The table is initially populated with Multum content but a client has the ability to modify the Multum content and build their own.

**Description:** It is used to hold content updates and versioning of dose range rules.  
**Table type:** REFERENCE  
**Primary key:** `DOSE_RANGE_CHECK_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BUILD_FLAG` | DOUBLE |  |  | This tells us who built the relationship. |
| 3 | `CONTENT_RULE_IDENTIFIER` | DOUBLE |  |  | If the rule was created by Multum or another content provider an identifier that can be used in handling updates. |
| 4 | `DOSE_RANGE_CHECK_ID` | DOUBLE | NOT NULL | PK | Unique identifier |
| 5 | `DOSE_RANGE_CHECK_NAME` | VARCHAR(100) |  |  | A textual description of the rule to allow easier viewing and building of DRC functionality. |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | A pointer to a set of text that a site could build to display to their users at DRC message time. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DRC_FACILITY_R](DRC_FACILITY_R.md) | `DOSE_RANGE_CHECK_ID` |
| [DRC_FACILITY_R_VER](DRC_FACILITY_R_VER.md) | `DOSE_RANGE_CHECK_ID` |

