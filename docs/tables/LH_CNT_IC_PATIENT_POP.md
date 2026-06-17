# LH_CNT_IC_PATIENT_POP

> This table stores the infection control patient population

**Description:** LIGHTHOUSE CONTENT INFECTION CONTROL PATIENT POPULATION  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_IC_PATIENT_POP_ID`  
**Columns:** 23  
**Referenced by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEVICE_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient had device data that caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encntr_id of the patient. |
| 4 | `FECAL_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient had fecal data that caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |
| 5 | `ISOLATION_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient had isolation data that caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |
| 6 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_POP table. |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The facility for the patient's encounter. |
| 8 | `MICRO_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient had micro data that caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |
| 9 | `NOTIF_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient had notification data that caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |
| 10 | `PATIENT_GROUP_DT_TM` | DATETIME |  |  | This is the date/time the patient was manually moved to the Ongoing assessment or Deleted categories. It should be NULL if the patient_group_flag is 0 or 1. |
| 11 | `PATIENT_GROUP_FLAG` | DOUBLE | NOT NULL |  | This flag is used to assign patients to groups used by Infection Preventionists for organizing the level of care needed. 0=Default value, no group assigned, 1=Needs Assessment, 2=Ongoing Assessment, 3=No longer being assessed/deleted |
| 12 | `PATIENT_INFO_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient info data caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |
| 13 | `PERFORMED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the user who triggered the patient to be added to this table. The triggering occurs by a Discern rule when certain orders/clinical events occur. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the patient. |
| 15 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | This flag is used by an ops job to determine which patient's need to have data generated. 0= Do not process, 1=Process, 2=Current being processed |
| 16 | `RISK_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient had risk data that caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |
| 17 | `SERO_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient had serology data that caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `XRAY_TRIGGER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the patient had xray data that caused them to move to Needs Assessment category. 0=Not a triggering factor, 1=Triggering factor |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERFORMED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [LH_CNT_IC_PATIENT_DEVICE](LH_CNT_IC_PATIENT_DEVICE.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_FOLLOWUP](LH_CNT_IC_PATIENT_FOLLOWUP.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_HAI_RISK](LH_CNT_IC_PATIENT_HAI_RISK.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_INFO](LH_CNT_IC_PATIENT_INFO.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_ISOL](LH_CNT_IC_PATIENT_ISOL.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_LAB](LH_CNT_IC_PATIENT_LAB.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_MDRO_RSK](LH_CNT_IC_PATIENT_MDRO_RSK.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_NOTIF](LH_CNT_IC_PATIENT_NOTIF.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_POP_HIST](LH_CNT_IC_PATIENT_POP_HIST.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_READMIT](LH_CNT_IC_PATIENT_READMIT.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_READ_SRG](LH_CNT_IC_PATIENT_READ_SRG.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_RPT_RISK](LH_CNT_IC_PATIENT_RPT_RISK.md) | `LH_CNT_IC_PATIENT_POP_ID` |
| [LH_CNT_IC_PATIENT_XRAY](LH_CNT_IC_PATIENT_XRAY.md) | `LH_CNT_IC_PATIENT_POP_ID` |

