# LH_CNT_IC_VAE

> Infection Control VAE table.

**Description:** Lighthouse Content Infection Control Ventilator Associated Event  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_IC_VAE_ID`  
**Columns:** 29  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIT_DT_TM` | DATETIME |  |  | Admit Date of the patient |
| 2 | `APRV_IND` | DOUBLE |  |  | Indicator for APRV (Airway Pressure Release Ventilation). Set to 1 when there is APRV mode of ventilation present |
| 3 | `BSI_SECONDARY_IND` | DOUBLE |  |  | Indicator for a secondary Blood Stream Infection |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter ID from the encounter table |
| 5 | `EVENT_DT_TM` | DATETIME |  |  | Event Date of the VAE Event |
| 6 | `EVENT_LOC_CD` | DOUBLE | NOT NULL | FK→ | Location the VAE Event is attributed to. |
| 7 | `LH_CNT_IC_VAE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CNT_IC_VAE table. |
| 8 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location associated to the patient. |
| 9 | `LUNG_HIST_IND` | DOUBLE |  |  | Indicates if the patient qualifies for Lung Histopathology (1 = Positive, 0 = Negative). |
| 10 | `MANUAL_ADD_IND` | DOUBLE | NOT NULL |  | This column indicates a patient was manually added to the VAE population by a user. 0=System added,1=Manually added by user. |
| 11 | `MV_DT_TM` | DATETIME |  |  | Mechanical Ventiliation Date/Time |
| 12 | `MV_LOC_CD` | DOUBLE | NOT NULL | FK→ | Mechanical Ventiliation Location. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person ID from the person table |
| 14 | `PLEURAL_FLUID_IND` | DOUBLE |  |  | Indicates if the Pleural Fluid was obtained during Thoracentisis or Initial Chest Tube Insertion (1 = Yes, 0 = No). |
| 15 | `POST_PROC_CD` | DOUBLE | NOT NULL |  | Post Procedure VAE NHSN Code, populated if this record was related to Post Procedure VAE (as indicated in POST_PROC_IND). |
| 16 | `POST_PROC_DISP` | VARCHAR(255) |  |  | Post Procedure Display |
| 17 | `POST_PROC_DT_TM` | DATETIME |  |  | Post Procedure Data/Time |
| 18 | `POST_PROC_IND` | DOUBLE |  |  | Post Procedure Indicator |
| 19 | `REVIEWED_FLAG` | DOUBLE |  |  | Representation of what review state the patient is in.1 - Not Started2 - In Progress3 - Complete4 - Modified |
| 20 | `SUPPRESS_UNTIL_DT_TM` | DATETIME |  |  | This column stores the date/time that the VAE event will be suppressed until re-evaluation. Once this date exceeds current date/time, the event will be re-evaluated by the VAE ops job. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `VAE_CRITERIA_TXT` | VARCHAR(255) |  |  | Textual representation of the criteria for given VAE |
| 27 | `VAE_DEATH_IND` | DOUBLE |  |  | Indicator if the VAE contributed to the patients death |
| 28 | `VAE_START_DT_TM` | DATETIME |  |  | Start Date/Time of the VAE |
| 29 | `VAE_TYPE_FLAG` | DOUBLE |  |  | Indicates what grouping the patient falls in on the VAE Worklist.0 - Risk for VAE1 - VAC2 - IVAC3 - Possible VAP4 - Probable VAP5 - IVAC Patients with Positive Pleural Fluid Culture6 - IVAC Patients with Lung Histopathology Result7 - Patient Removed8 - No NHSN Event |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EVENT_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `MV_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_CNT_IC_VAE_EVENT_DTL](LH_CNT_IC_VAE_EVENT_DTL.md) | `LH_CNT_IC_VAE_ID` |
| [LH_CNT_IC_VAE_HIST](LH_CNT_IC_VAE_HIST.md) | `LH_CNT_IC_VAE_ID` |

