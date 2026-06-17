# DM_CMB_METADATA

> Host additional metadata for the combine framework

**Description:** DM_CMB_METADATA  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_ONLY_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate whether this combine should only apply to active rows. 0 = This combine should process active and inactive rows, which is the default behavior. 1 = This combine should only combine active rows.; |
| 2 | `CHILD_COLUMN` | VARCHAR(32) | NOT NULL |  | The column that will participate in combines on this table |
| 3 | `CHILD_CONS_NAME` | VARCHAR(32) |  |  | The optional name of the FK constraint for the child_column. |
| 4 | `CHILD_PE_NAME1_TXT` | VARCHAR(32) |  |  | The first optional value used to identify combinable data in the child_pe_name_column. |
| 5 | `CHILD_PE_NAME2_TXT` | VARCHAR(32) |  |  | The second optional value used to identify combinable data in the child_pe_name_column. |
| 6 | `CHILD_PE_NAME3_TXT` | VARCHAR(32) |  |  | The third optional value used to identify combinable data in the child_pe_name_column. |
| 7 | `CHILD_PE_NAME_COLUMN` | VARCHAR(32) |  |  | The optional parent_entity_name type column that relates to the child_column. |
| 8 | `CHILD_PK` | VARCHAR(32) | NOT NULL |  | The primary key column name for this table, which must be a single column primary key. |
| 9 | `CHILD_TABLE` | VARCHAR(32) | NOT NULL |  | The name of the combinable table |
| 10 | `COMBINE_ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Optional special action code for this combine, driven from CS 327. |
| 11 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted |
| 12 | `DM_CMB_METADATA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 13 | `PARENT_TABLE` | VARCHAR(32) | NOT NULL |  | Type of COMBINE this row relates to (i.e. PERSON, ENCOUNTER, PRSNL¿); |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

