# SERVICE_CATEGORY_HIST

> Records history of Service Catagory changes

**Description:** Service Catagory History  
**Table type:** ACTIVITY  
**Primary key:** `SVC_CAT_HIST_ID`  
**Columns:** 17  
**Referenced by:** 17 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTEND_PRSNL_ID` | DOUBLE |  |  | The personnel IDof the attending doc from the encntr_prsnl_reltn table. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `MED_SERVICE_CD` | DOUBLE |  |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 10 | `SERVICE_CATEGORY_CD` | DOUBLE |  |  | Codified field which identifies the current category of service the patient is receiving. |
| 11 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for this table. |
| 12 | `TRANSACTION_DT_TM` | DATETIME |  |  | Date and Time the transaction was processed |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (17)

| From table | Column |
|------------|--------|
| [ABSTRACTING](ABSTRACTING.md) | `SVC_CAT_HIST_ID` |
| [ABSTRACT_DATA](ABSTRACT_DATA.md) | `SVC_CAT_HIST_ID` |
| [ABST_CODING_RELTN](ABST_CODING_RELTN.md) | `SVC_CAT_HIST_ID` |
| [CAC_DOCUMENT](CAC_DOCUMENT.md) | `SVC_CAT_HIST_ID` |
| [CODING](CODING.md) | `SVC_CAT_HIST_ID` |
| [CODING_AUDIT](CODING_AUDIT.md) | `SVC_CAT_HIST_ID` |
| [CODING_HIST](CODING_HIST.md) | `SVC_CAT_HIST_ID` |
| [CODING_SPECIALTY](CODING_SPECIALTY.md) | `SVC_CAT_HIST_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `SVC_CAT_HIST_ID` |
| [DIAGNOSIS_HIST](DIAGNOSIS_HIST.md) | `SVC_CAT_HIST_ID` |
| [DRG](DRG.md) | `SVC_CAT_HIST_ID` |
| [DRG_ENCNTR_EXTENSION](DRG_ENCNTR_EXTENSION.md) | `SVC_CAT_HIST_ID` |
| [DRG_SPECIALTY](DRG_SPECIALTY.md) | `SVC_CAT_HIST_ID` |
| [EEM_BENEFIT_ALLOC](EEM_BENEFIT_ALLOC.md) | `SVC_CAT_HIST_ID` |
| [NOMENCLATURE_ENCNTR_DESC](NOMENCLATURE_ENCNTR_DESC.md) | `SVC_CAT_HIST_ID` |
| [PROCEDURE](PROCEDURE.md) | `SVC_CAT_HIST_ID` |
| [PROCEDURE_HIST](PROCEDURE_HIST.md) | `SVC_CAT_HIST_ID` |

