# DM_PK_WHERE_LOCAL

> Stores templates of PK_WHERE forms to be used by RDDS for each table locally

**Description:** Database Management PK where Local  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DELETE_IND` | DOUBLE | NOT NULL |  | Indicates if template is for Delete PK_WHERE |
| 2 | `MERGE_DELETE_IND` | DOUBLE | NOT NULL |  | Indicates if template is for Merge Delete Table |
| 3 | `PK_WHERE_FUNCTION_IND` | DOUBLE | NOT NULL |  | Indicates whether template column holds function call |
| 4 | `PK_WHERE_PARM_QUERY` | VARCHAR(500) |  |  | Holds query used to get parameters for PK_WHERE template |
| 5 | `PK_WHERE_TEMPLATE` | VARCHAR(2000) | NOT NULL |  | Holds PK_WHERE Template |
| 6 | `PK_WHERE_WHERE_QUERY` | VARCHAR(500) |  |  | Holds Query used to create PK_WHERE template |
| 7 | `PTAM_MATCH_FUNCTION_IND` | DOUBLE | NOT NULL |  | Indicates whether template column holds function call |
| 8 | `PTAM_MATCH_PARM_QUERY` | VARCHAR(500) |  |  | Holds query used to get parameters for PTAM Match template |
| 9 | `PTAM_MATCH_TEMPLATE` | VARCHAR(2000) | NOT NULL |  | Holds PTAM Match Template |
| 10 | `PTAM_MATCH_WHERE_QUERY` | VARCHAR(500) |  |  | Holds query used to get PTAM Match template |
| 11 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Holds table name that uses template |
| 12 | `TEMPLATE_ID` | DOUBLE | NOT NULL |  | Identifier assigned internally of PK_WHERE form |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERSION_ALG` | VARCHAR(12) |  |  | Indicates type of versioning template |
| 19 | `VERSION_IND` | DOUBLE | NOT NULL |  | Indicates if template is for versioning table |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

