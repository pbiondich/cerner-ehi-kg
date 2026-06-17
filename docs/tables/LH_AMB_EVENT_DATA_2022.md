# LH_AMB_EVENT_DATA_2022

> Table containing event information for meaningful use NQF stage 2 2022.

**Description:** LH_AMB_EVENT_DATA_2022  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 45

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSOCIATED_ENTITY_ID` | DOUBLE |  |  | The ID of the associated event from the table listed in associated_entity_name. |
| 3 | `ASSOCIATED_ENTITY_NAME` | VARCHAR(30) |  |  | The name of the table the associated event in the associated_entity_id column is coming from. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `BR_DATAM_VSET_ITEM_ID` | DOUBLE |  |  | References the id in BR_DATAM_VSET_ITEM. |
| 6 | `BR_DATAM_VSET_ITEM_NEG_ID` | DOUBLE |  |  | References the negation in BR_DATAM_VSET_ITEM. |
| 7 | `CE_RESULT_UNIT` | VARCHAR(50) |  |  | The unit of the result value. |
| 8 | `CE_RESULT_VAL` | VARCHAR(255) |  |  | The value of the result |
| 9 | `DIAG_ACTIVE_IND` | DOUBLE |  |  | Table row is active or inactive |
| 10 | `DIAG_PRIORITY` | DOUBLE |  |  | Priority of diagnoses as determined by application |
| 11 | `D_QUERY_ID` | DOUBLE |  | FK→ | Identifies the query associated with the quality measure. Foreign key to the LH_D_QUERY table. |
| 12 | `ENCNTR_ID` | DOUBLE |  |  | Identifies the encounter against which the quality measure is associated. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EP_DT_TM` | DATETIME |  |  | Activity date/time of an event. |
| 15 | `EP_END_DT_TM` | DATETIME |  |  | The date and time the Diagnosis/Problem/Prcedure/order end. |
| 16 | `EXTRACT_DT_TM` | DATETIME |  |  | The time in which the nqf load script that updated this record was run |
| 17 | `FAMILY_MBR_CODE` | VARCHAR(255) |  |  | Family member associated with the patient for family history diagnosis |
| 18 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 19 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Identifies the delivery network responsible for supplying the data. |
| 20 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 21 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 22 | `LAST_UPDATED_PROVIDER_ID` | DOUBLE |  |  | This gives the ID of the provider whoever has updated the row last |
| 23 | `LH_AMB_EVENT_DATA_2022_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_EVENT_DATA_2022 table. |
| 24 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether the given result code is a negation or not (QRDA) |
| 25 | `ONSET_DT_TM` | DATETIME |  |  | The date and time the problem began |
| 26 | `PARENT_ENTITY_ID` | DOUBLE |  |  | The ID of the event type from parent_entity_name. |
| 27 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The table name of the parent_entity_id source. |
| 28 | `PERSON_ID` | DOUBLE |  |  | Identifies the person associated with the quality measure. |
| 29 | `POP_REG_DT_TM` | DATETIME |  |  | The date of the qualifying encounter that corresponds to this record. |
| 30 | `PRIMARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the encounter type (QRDA) |
| 31 | `PRIMARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the encounter type (QRDA) |
| 32 | `PRIMARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the encounter type (QRDA) |
| 33 | `PRIMARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the encounter type (QRDA) |
| 34 | `PRIMARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the encounter code system's value set (QRDA) |
| 35 | `PROB_LIFE_CYCLE_STATUS_CD` | DOUBLE |  |  | The current status of the problem. (From Problem Table) |
| 36 | `QUAL_REG_DT_TM` | DATETIME |  |  | Indicates the date of a candidate for deletion. |
| 37 | `SECONDARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the result type (QRDA) |
| 38 | `SECONDARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the result type (QRDA) |
| 39 | `SECONDARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the result type (QRDA) |
| 40 | `SECONDARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the result type (QRDA) |
| 41 | `SECONDARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the result code system's value set (QRDA) |
| 42 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 45 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_QUERY_ID` | [LH_D_QUERY](LH_D_QUERY.md) | `D_QUERY_ID` |

