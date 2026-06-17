# LH_AMB_QUAL_ENCNTR_2017

> Table containing the qualifying encounters for Meaningful Use NQF Stage 2 2017

**Description:** LH_AMB_QUAL_ENCNTR_2017  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 62

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BR_DATAM_VSET_ITEM_ID` | DOUBLE | NOT NULL |  | References the id in BR_DATAM_VSET_ITEM. |
| 3 | `BR_DATAM_VSET_ITEM_NEG_ID` | DOUBLE | NOT NULL |  | References the negation in BR_DATAM_VSET_ITEM. |
| 4 | `CMS_PAYER_GROUP` | VARCHAR(100) |  |  | The CMS payer grouping of the patient's payer. |
| 5 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 6 | `DISCH_DT_TM` | DATETIME |  |  | The date/time of patient discharge |
| 7 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON table. |
| 8 | `D_QUERY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the query associated with the quality measure. Foreign key to the LH_D_QUERY table. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 10 | `ETHNICITY_VSET_CD` | VARCHAR(100) |  |  | The code value corresponding to the patient's ethnicity. |
| 11 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 12 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 13 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 14 | `GENDER_VSET_CD` | VARCHAR(100) |  |  | The code value corresponding to the patient's gender. |
| 15 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL |  | The identifier for the patient¿s health plan |
| 16 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 17 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 18 | `HIC_NBR` | VARCHAR(50) |  |  | The patient's HIC number. |
| 19 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 20 | `LH_AMB_QUAL_ENCNTR_2017_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_QUAL_ENCNTR_2017 table. |
| 21 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The code value corresponding to the nursing unit of the encounter. |
| 22 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 23 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether the given result code is a negation or not (QRDA) |
| 24 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | References the id in ORGANIZATION. |
| 25 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 26 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the event type from parent_entity_name. |
| 27 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The table name of the parent_entity_id source. |
| 28 | `PAYER_VSET_CD` | VARCHAR(100) |  |  | The code value corresponding to the patient's payer. |
| 29 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(100) |  |  | The textual representation of the patient's ethnicity |
| 30 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(100) |  |  | The code system of the patient's ethnicity |
| 31 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(100) |  |  | The name of the patient's ethnicity code system |
| 32 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(100) |  |  | The textual representation of the patient's gender |
| 33 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(100) |  |  | The code system of the patient's gender |
| 34 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(100) |  |  | The name of the patient's gender code system |
| 35 | `PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person against which the qualify measure is associated. |
| 36 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(100) |  |  | Text description of the policy type |
| 37 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(100) |  |  | String representation of the code system that policy was derived from |
| 38 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(100) |  |  | The name of the policy code system. |
| 39 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(100) |  |  | The textual representation of the patient's race |
| 40 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(100) |  |  | The code system of the patient's race |
| 41 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(100) |  |  | The name of the patient's race code system |
| 42 | `POLICY_TYPE_DISPLAY` | VARCHAR(100) |  |  | Text description of the policy type |
| 43 | `POLICY_TYPE_SYSTEM_SDTC` | VARCHAR(100) |  |  | OID of codeSystem string. |
| 44 | `POP_EP_DT_TM` | DATETIME |  |  | Activity date/time of an event qualifying in population. |
| 45 | `PQRS_IND` | DOUBLE |  |  | Indicates whether the patient qualifies for PQRS. |
| 46 | `PRIMARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the encounter type (QRDA) |
| 47 | `PRIMARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the encounter type (QRDA) |
| 48 | `PRIMARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the encounter type (QRDA) |
| 49 | `PRIMARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the encounter type (QRDA) |
| 50 | `PRIMARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the encounter code system's value set (QRDA) |
| 51 | `QUAL_REG_DT_TM` | DATETIME |  |  | Indicates the date of a candidate for deletion. |
| 52 | `RACE_VSET_CD` | VARCHAR(100) |  |  | The code value corresponding to the patient's race. |
| 53 | `REG_DT_TM` | DATETIME |  |  | Registration date/time of encounter. |
| 54 | `SECONDARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the result type (QRDA) |
| 55 | `SECONDARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the result type (QRDA) |
| 56 | `SECONDARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the result type (QRDA) |
| 57 | `SECONDARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the result type (QRDA) |
| 58 | `SECONDARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the result code system's value set (QRDA) |
| 59 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 62 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_QUERY_ID` | [LH_D_QUERY](LH_D_QUERY.md) | `D_QUERY_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |

