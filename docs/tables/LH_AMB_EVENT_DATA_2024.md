# LH_AMB_EVENT_DATA_2024

> Table containing event information for meaningful use NQF stage 2 2024.

**Description:** LH_AMB_EVENT_DATA_2024  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 56

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
| 23 | `LH_AMB_EVENT_DATA_2024_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_EVENT_DATA_2024 table. |
| 24 | `MEDS_DISPENSE_QTY` | DOUBLE |  |  | This field contains the dispense quantity of the medication. |
| 25 | `MEDS_DISPENSE_QTY_UNIT` | VARCHAR(100) |  |  | This field contains the unit of the dispense quantity of medication. |
| 26 | `MEDS_DURATION` | DOUBLE |  |  | This field contains the duration for medication. |
| 27 | `MEDS_DURATION_UNIT` | VARCHAR(100) |  |  | This field contains the unit for duration of the medication. |
| 28 | `MEDS_FREQUENCY` | DOUBLE |  |  | This field contains the frequency of the medication. |
| 29 | `MEDS_REFILL_CNT` | DOUBLE |  |  | This field contains the refill count of the medication. |
| 30 | `MEDS_STRENGTH_DOSE` | DOUBLE |  |  | This field contains medication dose's strength. |
| 31 | `MEDS_STRENGTH_DOSE_UNIT` | VARCHAR(100) |  |  | This field contains the unit of the medication dose's strength. |
| 32 | `MEDS_VOLUME_DOSE` | DOUBLE |  |  | This field contains medication dose's volume. |
| 33 | `MEDS_VOLUME_DOSE_UNIT` | VARCHAR(100) |  |  | This field contains the unit of the medication dose's volume. |
| 34 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether the given result code is a negation or not (QRDA) |
| 35 | `ONSET_DT_TM` | DATETIME |  |  | The date and time the problem began |
| 36 | `PARENT_ENTITY_ID` | DOUBLE |  |  | The ID of the event type from parent_entity_name. |
| 37 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The table name of the parent_entity_id source. |
| 38 | `PERSON_ID` | DOUBLE |  |  | Identifies the person associated with the quality measure. |
| 39 | `POP_REG_DT_TM` | DATETIME |  |  | The date of the qualifying encounter that corresponds to this record. |
| 40 | `PRIMARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the encounter type (QRDA) |
| 41 | `PRIMARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the encounter type (QRDA) |
| 42 | `PRIMARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the encounter type (QRDA) |
| 43 | `PRIMARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the encounter type (QRDA) |
| 44 | `PRIMARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the encounter code system's value set (QRDA) |
| 45 | `PROB_LIFE_CYCLE_STATUS_CD` | DOUBLE |  |  | The current status of the problem. (From Problem Table) |
| 46 | `QUAL_REG_DT_TM` | DATETIME |  |  | Indicates the date of a candidate for deletion. |
| 47 | `SECONDARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the result type (QRDA) |
| 48 | `SECONDARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the result type (QRDA) |
| 49 | `SECONDARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the result type (QRDA) |
| 50 | `SECONDARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the result type (QRDA) |
| 51 | `SECONDARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the result code system's value set (QRDA) |
| 52 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 55 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `VACCINE_DOSE_FLAG` | DOUBLE |  |  | This field contains the details of vaccine dose. 0 - Row is not related to a vaccine dose, 2 - This value will denote a 2-dose vaccine, 3 - This value will denote a 3-dose vaccine, 4 - This value will denote a 4-dose vaccine. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_QUERY_ID` | [LH_D_QUERY](LH_D_QUERY.md) | `D_QUERY_ID` |

