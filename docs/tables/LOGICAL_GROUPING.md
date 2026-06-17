# LOGICAL_GROUPING

> This table contains locical groupings of data elements, primarily for privilege definition. Elements of the grouping are stored on the LOG_GROUP_ENTRY table.

**Description:** This table contains locical groupings of data elements, primarily for privileges  
**Table type:** REFERENCE  
**Primary key:** `LOG_GROUPING_CD`  
**Columns:** 9  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMP_TYPE_CD` | DOUBLE | NOT NULL |  | This row contains the code value representing the type of element that is being grouped (i.e. orders, discretes,...) |
| 2 | `LOGICAL_GROUP_DESC` | VARCHAR(100) |  |  | This column will contain a description of the logical grouping. |
| 3 | `LOG_GROUPING_CD` | DOUBLE | NOT NULL | PK | This column contains the unique identifier of a row on this table. |
| 4 | `LOG_GROUPING_TYPE_CD` | DOUBLE | NOT NULL |  | This column contains a code value representing the type or the use of this logical grouping, i.e. privileges. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [LOG_GROUP_ENTRY](LOG_GROUP_ENTRY.md) | `LOG_GROUPING_CD` |
| [LOG_GROUP_TYPE](LOG_GROUP_TYPE.md) | `LOG_GROUPING_CD` |
| [PRIVILEGE](PRIVILEGE.md) | `LOG_GROUPING_CD` |
| [PRIV_GROUP_RELTN](PRIV_GROUP_RELTN.md) | `LOG_GROUPING_CD` |

