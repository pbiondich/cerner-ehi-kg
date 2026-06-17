# GROUP_TYPE

> Group Types for the OMF Grouping Tool.

**Description:** GROUP TYPE  
**Table type:** REFERENCE  
**Primary key:** `GROUPING_CD`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DELETE_SCRIPT` | VARCHAR(255) |  |  | Script to use to delete from this group type. |
| 2 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of group type. |
| 3 | `GROUPING_CD` | DOUBLE | NOT NULL | PK | Group type code value. |
| 4 | `MGMT_CD` | DOUBLE | NOT NULL |  | Determines the product group this group type belongs to. |
| 5 | `NUM_KEYS` | DOUBLE |  |  | Number of values used in key. |
| 6 | `STATUS_IND` | DOUBLE |  |  | Determines whether the Group Type is active. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_INSERT_SCRIPT` | VARCHAR(255) |  |  | Request number of script used to update or insert a group member. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [GROUP_TYPE_KEYS](GROUP_TYPE_KEYS.md) | `GROUPING_CD` |

