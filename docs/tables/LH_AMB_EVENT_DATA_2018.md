# LH_AMB_EVENT_DATA_2018

> Table containing event information for meaningful use NQF stage 2 2018

**Description:** LH_AMB_EVENT_DATA_2018  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 43

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_DATAM_VSET_ITEM_ID` | DOUBLE | NOT NULL |  | References the id in BR_DATAM_VSET_ITEM. |
| 4 | `BR_DATAM_VSET_ITEM_NEG_ID` | DOUBLE | NOT NULL |  | References the negation in BR_DATAM_VSET_ITEM. |
| 5 | `CE_RESULT_UNIT` | VARCHAR(50) |  |  | The unit of the result value. |
| 6 | `CE_RESULT_VAL` | VARCHAR(255) |  |  | The value of the result |
| 7 | `DIAG_ACTIVE_IND` | DOUBLE |  |  | Table row is active or inactive |
| 8 | `DIAG_PRIORITY` | DOUBLE |  |  | Priority of diagnoses as determined by application |
| 9 | `D_QUERY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the query associated with the quality measure. Foreign key to the LH_D_QUERY table. |
| 10 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EP_DT_TM` | DATETIME |  |  | Activity date/time of an event. |
| 13 | `EP_END_DT_TM` | DATETIME |  |  | The date and time the Diagnosis/Problem/Prcedure/order end. |
| 14 | `EXTRACT_DT_TM` | DATETIME |  |  | The time in which the nqf load script that updated this record was run |
| 15 | `FAMILY_MBR_CODE` | VARCHAR(255) |  |  | Family member associated with the patient for family history diagnosis |
| 16 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 17 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 18 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 19 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 20 | `LAST_UPDATED_PROVIDER_ID` | DOUBLE | NOT NULL |  | The id representing the provider on the last action of the order where it was present. |
| 21 | `LH_AMB_EVENT_DATA_2018_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_EVENT_DATA_2018 table. |
| 22 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether the given result code is a negation or not (QRDA) |
| 23 | `ONSET_DT_TM` | DATETIME |  |  | The date and time the problem began |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the event type from parent_entity_name. |
| 25 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The table name of the parent_entity_id source. |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. |
| 27 | `POP_REG_DT_TM` | DATETIME |  |  | The date of the qualifying encounter that corresponds to this record. |
| 28 | `PRIMARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the encounter type (QRDA) |
| 29 | `PRIMARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the encounter type (QRDA) |
| 30 | `PRIMARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the encounter type (QRDA) |
| 31 | `PRIMARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the encounter type (QRDA) |
| 32 | `PRIMARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the encounter code system's value set (QRDA) |
| 33 | `PROB_LIFE_CYCLE_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the problem. (From Problem Table) |
| 34 | `QUAL_REG_DT_TM` | DATETIME |  |  | Indicates the date of a candidate for deletion. |
| 35 | `SECONDARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the result type (QRDA) |
| 36 | `SECONDARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the result type (QRDA) |
| 37 | `SECONDARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the result type (QRDA) |
| 38 | `SECONDARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the result type (QRDA) |
| 39 | `SECONDARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the result code system's value set (QRDA) |
| 40 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 43 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_QUERY_ID` | [LH_D_QUERY](LH_D_QUERY.md) | `D_QUERY_ID` |

