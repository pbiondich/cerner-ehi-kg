# ENCNTR_SLICE

> Stores different slices of time for an encounter (i.e. Consultant Epsiodes)

**Description:** Encounter Slice  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_SLICE_ID`  
**Columns:** 15  
**Referenced by:** 21 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Associated Encounter for the time slice |
| 7 | `ENCNTR_SLICE_FLAG` | DOUBLE | NOT NULL |  | Encounter slice origin and update activity 0 - Normal Process; 1 - Upload from service_cat_hist table; 2 - Insert from Encntr Slice Viewer; 3 - Update from Encntr Slice Viewer; 4 - Removed from Encntr Slice Viewer |
| 8 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | PK | Identifies an Encounter as it relates to a time slice. |
| 9 | `ENCNTR_SLICE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of slice that is being recorded for an Encounter. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (21)

| From table | Column |
|------------|--------|
| [ABSTRACTING](ABSTRACTING.md) | `ENCNTR_SLICE_ID` |
| [ABSTRACT_DATA](ABSTRACT_DATA.md) | `ENCNTR_SLICE_ID` |
| [ABST_CODING_RELTN](ABST_CODING_RELTN.md) | `ENCNTR_SLICE_ID` |
| [CAC_DOCUMENT](CAC_DOCUMENT.md) | `ENCNTR_SLICE_ID` |
| [CODING](CODING.md) | `ENCNTR_SLICE_ID` |
| [CODING_AUDIT](CODING_AUDIT.md) | `ENCNTR_SLICE_ID` |
| [CODING_HIST](CODING_HIST.md) | `ENCNTR_SLICE_ID` |
| [CODING_SPECIALTY](CODING_SPECIALTY.md) | `ENCNTR_SLICE_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `ENCNTR_SLICE_ID` |
| [DIAGNOSIS_HIST](DIAGNOSIS_HIST.md) | `ENCNTR_SLICE_ID` |
| [DRG](DRG.md) | `ENCNTR_SLICE_ID` |
| [DRG_ENCNTR_EXTENSION](DRG_ENCNTR_EXTENSION.md) | `ENCNTR_SLICE_ID` |
| [DRG_SPECIALTY](DRG_SPECIALTY.md) | `ENCNTR_SLICE_ID` |
| [EEM_BENEFIT_ALLOC](EEM_BENEFIT_ALLOC.md) | `ENCNTR_SLICE_ID` |
| [ENCNTR_AUGM_CARE_PERIOD](ENCNTR_AUGM_CARE_PERIOD.md) | `ENCNTR_SLICE_ID` |
| [ENCNTR_SLICE_ACT](ENCNTR_SLICE_ACT.md) | `ENCNTR_SLICE_ID` |
| [ENCNTR_SLICE_HIST](ENCNTR_SLICE_HIST.md) | `ENCNTR_SLICE_ID` |
| [NOMENCLATURE_ENCNTR_DESC](NOMENCLATURE_ENCNTR_DESC.md) | `ENCNTR_SLICE_ID` |
| [PM_POST_PROCESS](PM_POST_PROCESS.md) | `ENCNTR_SLICE_ID` |
| [PROCEDURE](PROCEDURE.md) | `ENCNTR_SLICE_ID` |
| [PROCEDURE_HIST](PROCEDURE_HIST.md) | `ENCNTR_SLICE_ID` |

