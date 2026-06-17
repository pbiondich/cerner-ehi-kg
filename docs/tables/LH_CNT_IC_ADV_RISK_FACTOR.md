# LH_CNT_IC_ADV_RISK_FACTOR

> Stores the risk factors saved within the Risk Factors component of the IC Advisor.

**Description:** LH_CNT_IC_ADV_RISK_FACTOR  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BIRTHWEIGHT_IN_GRAMS` | VARCHAR(255) |  |  | The birthweight of the patient in grams. Value to be submitted to NHSN. |
| 4 | `CENTRAL_LINE_FLAG` | DOUBLE | NOT NULL |  | Indicates selection of the ""Central Line"" radio button. 0 - Unknown, 1 - Yes, 2 - No |
| 5 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the EKS_ADVSR_EVENT table. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `INSERTION_DT_TM` | DATETIME |  |  | Date and time of insertion of the device. |
| 8 | `INSERTION_LOC_CD` | DOUBLE | NOT NULL |  | Location code of where the device was inserted. |
| 9 | `LH_CNT_IC_ADV_RISK_FACTOR_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_ADV_RISK_FACTOR table. |
| 10 | `LOCATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the NHSN location type at the moment of save, per the bedrock settings. 0 - Unknown, 1 - NICU, 2 - ICU, 3 - SCA. |
| 11 | `PERM_CENTRAL_LINE_FLAG` | DOUBLE | NOT NULL |  | Indicates selection of the ""Permanent Central Line"" radio button. 0 - Unknown, 1 - Yes, 2 - No |
| 12 | `TEMP_CENTRAL_LINE_FLAG` | DOUBLE | NOT NULL |  | Indicates selection of the ""Temporary Central Line"" radio button. 0 - Unknown, 1 - Yes, 2 - No |
| 13 | `UMBILICAL_LINE_FLAG` | DOUBLE | NOT NULL |  | Indicates selection of the ""Central Line(including umbilical catheter)"" radio button. 0 - Unknown, 1 - Yes, 2 - No |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `URINARY_CATHETER_FLAG` | DOUBLE | NOT NULL |  | Indicates selection from within the Urinary Catheter radio group. 0 = Nothing Selected(not a UTI), 1 = "In Place", 2 = "Removed within 2 days prior", 3 = "Neither". |
| 20 | `VENTILATOR_FLAG` | DOUBLE | NOT NULL |  | Indicates selection of the ""Ventilator"" radio button. 0 - Unknown, 1 - Yes, 2 - No |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |

