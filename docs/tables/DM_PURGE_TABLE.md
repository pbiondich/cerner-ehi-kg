# DM_PURGE_TABLE

> Table relationships for purge templates.

**Description:** DM PURGE TABLE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COL1` | VARCHAR(30) |  |  | Child join column 1. |
| 2 | `CHILD_COL2` | VARCHAR(30) |  |  | Child join column 2. |
| 3 | `CHILD_COL3` | VARCHAR(30) |  |  | Child join column 3. |
| 4 | `CHILD_COL4` | VARCHAR(30) |  |  | Child join column 4. |
| 5 | `CHILD_COL5` | VARCHAR(30) |  |  | Child join column 5. |
| 6 | `CHILD_TABLE` | VARCHAR(30) |  |  | Child table. |
| 7 | `CHILD_WHERE` | VARCHAR(255) |  |  | Where clause to attach when performing a purge on the child table. |
| 8 | `FEATURE_NBR` | DOUBLE |  |  | Rev Tool Feature number to which this purge template was promoted. |
| 9 | `PARENT_COL1` | VARCHAR(30) |  |  | Parent join column 1. |
| 10 | `PARENT_COL2` | VARCHAR(30) |  |  | Parent join column 2. |
| 11 | `PARENT_COL3` | VARCHAR(30) |  |  | Parent join column 3. |
| 12 | `PARENT_COL4` | VARCHAR(30) |  |  | Parent join column 4. |
| 13 | `PARENT_COL5` | VARCHAR(30) |  |  | Parent join column 5. |
| 14 | `PARENT_TABLE` | VARCHAR(30) |  |  | Parent table. |
| 15 | `PURGE_TYPE_FLAG` | DOUBLE |  |  | Purge Type. 0 - indicative of a root table in a purge template's table hierarchy; 1 - Data will be deleted from child table; 2 - All inherited values on the child table will be set to 0, effectively disassociating the child row from the parent row; 5 - indicative of a root table in an XNT template's table hierarchy; 6 - indicative of a child table in an XNT template's table hierarchy. |
| 16 | `SCHEMA_DT_TM` | DATETIME |  |  | Date/time this purge template modification was promoted in Feature Tracker. |
| 17 | `TEMPLATE_NBR` | DOUBLE |  |  | Number (id) of the purge template that this job uses. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

