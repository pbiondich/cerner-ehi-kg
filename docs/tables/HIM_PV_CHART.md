# HIM_PV_CHART

> Visit information for Powervision

**Description:** HIM PV CHART  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMITTING_PERSON_ID` | DOUBLE | NOT NULL |  | Person_Id of the admitting physician |
| 2 | `ALLOCATION_DT_FLAG` | DOUBLE |  |  | This flexes how allocation date is calculated |
| 3 | `ALLOCATION_DT_MODIFIER` | DOUBLE |  |  | The number of days to add to an event's date in calculating the allocation date. |
| 4 | `ALLOCATION_DT_TM` | DATETIME |  |  | Allocation date of the visit |
| 5 | `ATTENDING_PERSON_ID` | DOUBLE | NOT NULL |  | Person_Id of the attending physician |
| 6 | `BIRTH_DT_TM` | DATETIME |  |  | Birth date of the patient |
| 7 | `CHART_AGE` | DOUBLE |  |  | Chart age of the visit |
| 8 | `CHART_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the visit |
| 9 | `CURRENT_LOC_CD` | DOUBLE | NOT NULL |  | Location of the chart |
| 10 | `DEFICIENCY_IND` | DOUBLE |  |  | Indicator that states if the chart is deficient |
| 11 | `DEF_ALLOCATION_DATE_IND` | DOUBLE |  |  | The indicator for any allocation date not equal to null |
| 12 | `DELINQUENT_IND` | DOUBLE |  |  | Indicator that states if the chart is delinquent |
| 13 | `DISCH_DT_TM` | DATETIME |  |  | Disch date of the visit |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 15 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Type of the visit (Inpatient, etc.) |
| 16 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class of the encounter |
| 17 | `HIM_PV_CHART_ID` | DOUBLE | NOT NULL |  | Unique identifier of the table |
| 18 | `MEDIA_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Unique id of the media from the media_master table |
| 19 | `MEDIA_TYPE_CD` | DOUBLE | NOT NULL |  | Type of the media |
| 20 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | Type of medical service |
| 21 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Id of the organization tied to the encounter |
| 22 | `ORG_NAME` | VARCHAR(100) |  |  | name of the organization tied to the encounter |
| 23 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 24 | `REG_DT_TM` | DATETIME |  |  | Admission date of the visit |
| 25 | `SEX_CD` | DOUBLE | NOT NULL |  | Sex of the patient |
| 26 | `SUSPENDED_IND` | DOUBLE |  |  | Indicator that tells if the chart is suspended |
| 27 | `TRACKING_ID` | VARCHAR(35) |  |  | Tracking id of the chart |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `VOLUME_NBR` | DOUBLE |  |  | Volume number of the chart |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MEDIA_MASTER_ID` | [MEDIA_MASTER](MEDIA_MASTER.md) | `MEDIA_MASTER_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

