# LH_AMB_QUAL_ENCNTR_2016

> Table containing the qualifying encounters for Meaningful Use NQF Stage 2 2016

**Description:** LH_AMB_QUAL_ENCNTR_2016  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 46

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BR_DATAM_VSET_ITEM_ID` | DOUBLE | NOT NULL |  | References the id in BR_DATAM_VSET_ITEM. |
| 3 | `BR_DATAM_VSET_ITEM_NEG_ID` | DOUBLE | NOT NULL |  | References the negation in BR_DATAM_VSET_ITEM. |
| 4 | `CMS_PAYER_GROUP` | VARCHAR(100) |  |  | The CMS payer grouping of the patient's payer. |
| 5 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 6 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON table. |
| 7 | `D_QUERY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the query associated with the quality measure. Foreign key to the LH_D_QUERY table. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 9 | `ETHNICITY_VSET_CD` | VARCHAR(100) |  |  | The code value corresponding to the patient's ethnicity. |
| 10 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 11 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 12 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The first date/time the row was updated by the NQF load script. |
| 13 | `GENDER_VSET_CD` | VARCHAR(100) |  |  | The code value corresponding to the patient's gender. |
| 14 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 15 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 16 | `HIC_NBR` | VARCHAR(50) |  |  | The patient's HIC number. |
| 17 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The last date/time the row was updated by the NQF load script. |
| 18 | `LH_AMB_QUAL_ENCNTR_2016_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_QUAL_ENCNTR_2016 table. |
| 19 | `LOC_NURSE_UNIT_CD` | DOUBLE |  |  | The code value corresponding to the nursing unit of the encounter. |
| 20 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 21 | `NEGATION_IND` | DOUBLE | NOT NULL |  | Indicates whether the given result code is a negation or not (QRDA) |
| 22 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | References the id in ORGANIZATION. |
| 23 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the event type from parent_entity_name. |
| 25 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The table name of the parent_entity_id source. |
| 26 | `PAYER_VSET_CD` | VARCHAR(100) |  |  | The code value corresponding to the patient's payer. |
| 27 | `PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person against which the qualify measure is associated. |
| 28 | `POP_EP_DT_TM` | DATETIME |  |  | Activity date/time of an event qualifying in population. |
| 29 | `PQRS_IND` | DOUBLE |  |  | Indicates whether the patient qualifies for PQRS. |
| 30 | `PRIMARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the encounter type (QRDA) |
| 31 | `PRIMARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the encounter type (QRDA) |
| 32 | `PRIMARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the encounter type (QRDA) |
| 33 | `PRIMARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the encounter type (QRDA) |
| 34 | `PRIMARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the encounter code system's value set (QRDA) |
| 35 | `QUAL_REG_DT_TM` | DATETIME |  |  | Indicates the date of a candidate for deletion. |
| 36 | `RACE_VSET_CD` | VARCHAR(100) |  |  | The code value corresponding to the patient's race. |
| 37 | `REG_DT_TM` | DATETIME |  |  | Registration date/time of encounter. |
| 38 | `SECONDARY_VSET_CD` | VARCHAR(100) |  |  | Code corresponding to the result type (QRDA) |
| 39 | `SECONDARY_VSET_CD_DISPLAY` | VARCHAR(500) |  |  | Detailed information on the result type (QRDA) |
| 40 | `SECONDARY_VSET_CD_SYS_NAME` | VARCHAR(100) |  |  | Coding system name for the result type (QRDA) |
| 41 | `SECONDARY_VSET_CD_SYS_OID` | VARCHAR(100) |  |  | Coding system of the result type (QRDA) |
| 42 | `SECONDARY_VSET_CD_SYS_SDTC` | VARCHAR(100) |  |  | The OID of the result code system's value set (QRDA) |
| 43 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 44 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 45 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 46 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_QUERY_ID` | [LH_D_QUERY](LH_D_QUERY.md) | `D_QUERY_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |

