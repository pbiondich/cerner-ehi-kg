# DM_TABLE_RELATIONSHIPS

> Reference table to store table relationships metadata

**Description:** DM_TABLE_RELATIONSHIPS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_RE_PK_NAME` | VARCHAR(50) |  |  | ALTERNATE ROOT ENTITY PK NAME |
| 2 | `ALT_RE_PK_POSITION` | DOUBLE |  |  | ALTERNATE ROOT ENTITY PK COLUMN POSITION |
| 3 | `ALT_ROOT_ENTITY_ATTR` | VARCHAR(30) |  |  | ALTERNATE ROOT ENTITY TABLE COLUMN NAME |
| 4 | `ALT_ROOT_ENTITY_NAME` | VARCHAR(30) |  |  | ALTERNATE ROOT ENTITY TABLE NAME |
| 5 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | COLUMN NAME PARTICIPATING IN THE RELATIONSHIP |
| 6 | `DM_TABLE_RELATIONSHIPS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `DRR_FLAG` | DOUBLE |  |  | FLAG to indicate if the row participates ( 1 ) or not ( -1 ) |
| 8 | `DRR_RELTN_TYPE` | VARCHAR(15) |  |  | Typically used to note of an ALTERNATIVE relationship is needed/used |
| 9 | `DRR_TABLE_NAME` | VARCHAR(30) |  |  | the name of the DRR shadow table |
| 10 | `DRR_TEXT` | VARCHAR(500) |  |  | store note on this relationship (comment) |
| 11 | `DRR_ZERO_PERSON_COL` | VARCHAR(30) |  |  | When DRR_RELTN_TYPE is ZERO, this column is populated with the other person column name that will be processed by standard method. |
| 12 | `DRR_ZERO_RESTORE_IND` | DOUBLE |  |  | When DRR_RELTN_TYPE is ZERO, this column will be populated 1 or 0. 1 - Unrestrict must restore original column value. |
| 13 | `EHI_FLAG` | DOUBLE |  |  | FLAG value for indicating able/column is processed for EHI ( -1 = does not participate, 1 = activity table participant 2 = = reference table participant ) |
| 14 | `FK_NAME` | VARCHAR(30) |  |  | for column in Foreign Key, this column will be populated with the Foreign Key name |
| 15 | `FK_POSITION` | DOUBLE |  |  | for column in Foreign Key, this column will be populated with the Foreign Key column position |
| 16 | `OWNER` | VARCHAR(20) | NOT NULL |  | TABLE OWNER |
| 17 | `PE_NAME_COLUMN` | VARCHAR(50) |  |  | for column has parent entity relationship, this column will be populated with column name that store parent table name. eg, PARENT_ENTITY_NAME |
| 18 | `PE_NAME_COL_VALUE` | VARCHAR(50) |  |  | for column has parent entity relationship, this column will be populated with parent table name. eg, PERSON |
| 19 | `PK_NAME` | VARCHAR(30) |  |  | for column in Primary Key, this column will be populated with the Primary Key name |
| 20 | `PK_POSITION` | DOUBLE |  |  | for column in Foreign Key, this column will be populated with the Foreign Key column position |
| 21 | `P_COLUMN_NAME` | VARCHAR(30) |  |  | store parent column name that has relationships with this column |
| 22 | `P_PK_NAME` | VARCHAR(30) |  |  | store parent table Primary Key name |
| 23 | `P_PK_POSITION` | DOUBLE |  |  | store parent table Primary Key column position |
| 24 | `P_TABLE_NAME` | VARCHAR(30) |  |  | store parent table name |
| 25 | `RE_PK_NAME` | VARCHAR(50) |  |  | store root parent's Primary Key name |
| 26 | `RE_PK_POSITION` | DOUBLE |  |  | store root parent's Primary Key position |
| 27 | `ROOT_ENTITY_ATTR` | VARCHAR(30) |  |  | store root parent column name |
| 28 | `ROOT_ENTITY_NAME` | VARCHAR(30) |  |  | Store root parent table name |
| 29 | `TABLE_INSTANCE` | DOUBLE | NOT NULL |  | table instance use for versioning. Should only have one max instance per table. |
| 30 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | THE TABLE NAME |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

