# LH_AMB_EVENT_DATA

> Table containing event information for Meaningful Use QM and PQRI solutions.

**Description:** LH_AMB_EVENT_DATA  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BR_DATAM_VSET_ITEM_ID` | DOUBLE | NOT NULL |  | This column will have br_datam_vset_item_id of an observation code, which will be used for QRDA XML files. |
| 3 | `BR_DATAM_VSET_ITEM_NEG_ID` | DOUBLE | NOT NULL |  | This column will have br_datam_vset_item_id of a Negation code, which will be used for QRDA XML files. |
| 4 | `D_QUERY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the query associated with the quality measure. Foreign key to the LH_D_QUERY table. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 6 | `EP_DT_TM` | DATETIME |  |  | Activity date/time of an event. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 9 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 10 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 12 | `LH_AMB_EVENT_DATA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_EVENT_DATA table. |
| 13 | `NEGATION_IND` | DOUBLE | NOT NULL |  | Indicates whether the given result code is a negation or not (QRDA) |
| 14 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the event type from parent_entity_name. |
| 15 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The table name of the parent_entity_id source. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. |
| 17 | `POP_REG_DT_TM` | DATETIME |  |  | Stores the registration date time of the encounter that qualified this row. This column is OBSOLETE. It has been replaced by column QUAL_REG_DT_TM. |
| 18 | `PRIMARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the encounter type (QRDA) |
| 19 | `PRIMARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the encounter type (QRDA) |
| 20 | `PRIMARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the encounter type (QRDA) |
| 21 | `PRIMARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the encounter type (QRDA) |
| 22 | `PRIMARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the encounter code system's value set (QRDA) |
| 23 | `QUAL_REG_DT_TM` | DATETIME |  |  | Stores the registration date time of the encounter that qualified this row. |
| 24 | `SECONDARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the result type (QRDA) |
| 25 | `SECONDARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the result type (QRDA) |
| 26 | `SECONDARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the result type (QRDA) |
| 27 | `SECONDARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the result type (QRDA) |
| 28 | `SECONDARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the result code system's value set (QRDA) |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 32 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_QUERY_ID` | [LH_D_QUERY](LH_D_QUERY.md) | `D_QUERY_ID` |

