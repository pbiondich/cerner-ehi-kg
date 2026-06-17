# DM_TABLE_RELATIONSHIPS_GTTP

> We will use this table as a temp table whose contents will later be loaded into DM_TABLE_RELATIONSHIPS table. So, this table needs to be identical to DM_TABLE_RELATIONSHIPS table.

**Description:** Global Temp table to facilitate load of DM_TABLE_RELATIONSHIPS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_RE_PK_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 2 | `ALT_RE_PK_POSITION` | DOUBLE |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 3 | `ALT_ROOT_ENTITY_ATTR` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 4 | `ALT_ROOT_ENTITY_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 5 | `COLUMN_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 6 | `DM_TABLE_RELATIONSHIPS_ID` | DOUBLE |  |  | PRIMARY KEY. Does not use sequence. ID value shipped from ADM table in RVADM1 |
| 7 | `DRR_FLAG` | DOUBLE |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 8 | `DRR_RELTN_TYPE` | VARCHAR(15) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 9 | `DRR_TABLE_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 10 | `DRR_TEXT` | VARCHAR(500) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 11 | `DRR_ZERO_PERSON_COL` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 12 | `DRR_ZERO_RESTORE_IND` | DOUBLE |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 13 | `EHI_FLAG` | DOUBLE |  |  | FLAG value for indicating able/column is processed for EHI ( -1 = does not participate, 1 = activity table participant 2 = = reference table participant ) |
| 14 | `FK_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 15 | `FK_POSITION` | DOUBLE |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 16 | `OWNER` | VARCHAR(20) |  |  | TABLE OWNER |
| 17 | `PE_NAME_COLUMN` | VARCHAR(50) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 18 | `PE_NAME_COL_VALUE` | VARCHAR(50) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 19 | `PK_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 20 | `PK_POSITION` | DOUBLE |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 21 | `P_COLUMN_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 22 | `P_PK_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 23 | `P_PK_POSITION` | DOUBLE |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 24 | `P_TABLE_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 25 | `RE_PK_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 26 | `RE_PK_POSITION` | DOUBLE |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 27 | `ROOT_ENTITY_ATTR` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 28 | `ROOT_ENTITY_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 29 | `TABLE_INSTANCE` | DOUBLE |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 30 | `TABLE_NAME` | VARCHAR(30) |  |  | See column doc content in DM_TABLE_RELATIONSHIPS |
| 31 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

