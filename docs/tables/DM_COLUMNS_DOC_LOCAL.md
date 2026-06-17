# DM_COLUMNS_DOC_LOCAL

> This table is a copy of the existing dm_columns_doc table that resides in admin

**Description:** DM COLUMNS DOC LOCAL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_SET` | DOUBLE |  |  | Code set |
| 2 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Column_name |
| 3 | `CONSTANT_VALUE` | VARCHAR(255) |  |  | Constant value |
| 4 | `DEFINING_ATTRIBUTE_IND` | DOUBLE |  |  | Defining_attribute_ind |
| 5 | `DEFINITION` | VARCHAR(500) |  |  | Definition |
| 6 | `DESCRIPTION` | VARCHAR(80) |  |  | Description |
| 7 | `EXCEPTION_FLG` | DOUBLE |  |  | Exception_Flg |
| 8 | `FLAG_IND` | DOUBLE |  |  | Flag_ind |
| 9 | `MERGE_DELETE_IND` | DOUBLE |  |  | Merge Delete Indicator |
| 10 | `MERGE_UPDATEABLE_IND` | DOUBLE |  |  | MERGE_UPDATEABLE_IND |
| 11 | `NLS_COL_IND` | DOUBLE |  |  | NLS_COL_IND |
| 12 | `PARENT_ENTITY_COL` | VARCHAR(30) |  |  | PARENT_ENTITY_COL |
| 13 | `ROOT_ENTITY_ATTR` | VARCHAR(30) |  |  | ROOT_ENTITY_ATTR |
| 14 | `ROOT_ENTITY_NAME` | VARCHAR(30) |  |  | ROOT_ENTITY_NAME |
| 15 | `SEQUENCE_NAME` | VARCHAR(30) |  |  | SEQUENCE_NAME |
| 16 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | TABLE_NAME |
| 17 | `UNIQUE_IDENT_IND` | DOUBLE |  |  | UNIQUE_IDENT_IND |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

