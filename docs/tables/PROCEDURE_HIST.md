# PROCEDURE_HIST

> Used to store history of procedures in Chart Coding

**Description:** Procedure History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ANESTHESIA_CD` | DOUBLE | NOT NULL |  | The type of anesthesia. |
| 3 | `ANESTHESIA_MINUTES` | DOUBLE |  |  | The number of minutes the patient was under anesthesia. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 6 | `DGVP_IND` | DOUBLE | NOT NULL |  | The number of minutes the patient was under anesthesia. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique identifier of the encounter table. It is an internal, system-assigned number |
| 8 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `GENERIC_VAL_CD` | DOUBLE | NOT NULL |  | Code value that is selected for the -Generic Field- in HIMChartCoding. |
| 11 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the primary identifier of the nomenclature table. It is an internal, system-assigned number. |
| 12 | `ORGANIZATION_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the Organization table. It is an internal system assigned number. The organization associated with this procedure. |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent table. |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent table name. |
| 15 | `PROCEDURE_HIST_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for a procedure history row. It is an internal, system-assigned number. |
| 16 | `PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier for a procedure row. It is an internal, system-assigned number. |
| 17 | `PROC_DT_TM` | DATETIME |  |  | The date and time the procedure was performed. |
| 18 | `PROC_LOC_CD` | DOUBLE | NOT NULL |  | The location code of the procedure. |
| 19 | `PROC_PRIORITY` | DOUBLE |  |  | The priority of the procedure compared to other procedures in the same encounter. |
| 20 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This field is a unique identifier for the service category history table. |
| 21 | `TISSUE_TYPE_CD` | DOUBLE | NOT NULL |  | The tissue type (for example, moist or supple). This is an optional field. |
| 22 | `UNITS_OF_SERVICE` | DOUBLE |  |  | The number of units of service for a procedure (i.e. units of blood). |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PROCEDURE_ID` | [PROCEDURE](PROCEDURE.md) | `PROCEDURE_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

