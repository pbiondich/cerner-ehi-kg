# PROCEDURE

> Stores the coded information for procedures from the patient's chart.

**Description:** Procedure Table  
**Table type:** ACTIVITY  
**Primary key:** `PROCEDURE_ID`  
**Columns:** 54  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ANESTHESIA_CD` | DOUBLE | NOT NULL |  | Anesthesia used for this procedure |
| 6 | `ANESTHESIA_MINUTES` | DOUBLE |  |  | The number of minutes the patient was under anesthesia |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CATEGORY_CD` | DOUBLE |  |  | This column will be used to store the category of a procedure which will be pulled from category codeset 4760259 to differentiate SDOH or NON SDOH. |
| 9 | `CLINICAL_SERVICE_CD` | DOUBLE | NOT NULL |  | It associates a procedure to a particular setting of care within an encounter. The unifying clinical trait of the notion of a clinical service is that it correlates to the physician's fiduciary responsibility for the patient as manifested by a formal hand-off / acceptance of care process that involves a declaration of diagnostic information that corresponds to the clinical service as the transition points. |
| 10 | `COMMENT_IND` | DOUBLE |  |  | Indicator that a comment was added about the procedure |
| 11 | `CONSENT_CD` | DOUBLE | NOT NULL |  | HL7 segment PR1-13 added on-the-fly.Definition: This field contains the type of consent that was obtained for permission to treat the patient. NOTE: This column is currently not being used but it may be used in the future. The Code Set for it does not exist either. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `DGVP_IND` | DOUBLE | NOT NULL |  | Indicator to determine whether or not a specific procedure was the Dominant Group variable Procedure for a given encounter or service category. 0 = not DVGP, 1 = DGVP |
| 14 | `DIAG_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the Nomenclature table. |
| 15 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 16 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `GENERIC_VAL_CD` | DOUBLE | NOT NULL |  | A code value that is the selected for the "Generic Field" in himChartCoding. |
| 19 | `LATERALITY_CD` | DOUBLE | NOT NULL |  | Identifies the code value associated with the laterality of the procedure. Code set 4002375 |
| 20 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | This is the unique identifier to the long text table. |
| 21 | `MOD_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The nomenclature Id of the nomenclature row used as a modifier |
| 22 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Nomenclature table. |
| 23 | `ORGANIZATION_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the Organization table. It is an internal system assigned number. The organization associated with this procedure. |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent table. |
| 25 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent table name. |
| 26 | `PROCEDURE_ID` | DOUBLE | NOT NULL | PK | Procedure id is the primary unique identification number of the procedure table. It is an internal system assigned sequence number. |
| 27 | `PROCEDURE_NOTE` | VARCHAR(255) |  |  | Free-text note for an individual procedure |
| 28 | `PROC_DT_TM` | DATETIME |  |  | The date and time when the procedure was performed. |
| 29 | `PROC_DT_TM_PREC_CD` | DOUBLE | NOT NULL |  | Used to indicate the precision selected by the end user when entering the procedure date & time (Before, After, About, Unknown, etc.) |
| 30 | `PROC_DT_TM_PREC_FLAG` | DOUBLE | NOT NULL |  | Precision flag for date and time.0 - Date or Date and Time, 1- Week, 2 - Month, 3 - Year. |
| 31 | `PROC_END_DT_TM` | DATETIME |  |  | The data and time the procedure was ended. |
| 32 | `PROC_FTDESC` | VARCHAR(255) |  |  | The free text field for a procedure. |
| 33 | `PROC_FT_DT_TM_IND` | DOUBLE |  |  | This indicator is set when a free textdata and time is entered |
| 34 | `PROC_FT_LOC` | VARCHAR(255) |  |  | This is free textlocation of the procedure. |
| 35 | `PROC_FT_TIME_FRAME` | VARCHAR(40) |  |  | This is the free texttime frame for the procedure |
| 36 | `PROC_FUNC_TYPE_CD` | DOUBLE | NOT NULL |  | The type of procedure function. An example would be anesthesia. |
| 37 | `PROC_LOC_CD` | DOUBLE | NOT NULL |  | This is the code_value associated with the location of the procedure. |
| 38 | `PROC_LOC_FT_IND` | DOUBLE |  |  | This is used to indicate if the location is a free text value. |
| 39 | `PROC_MINUTES` | DOUBLE |  |  | The amount of time in minutes the procedure took to complete. |
| 40 | `PROC_PRIORITY` | DOUBLE |  |  | The priority of the procedure compared to other procedures in the same encounter. |
| 41 | `PROC_START_DT_TM` | DATETIME |  |  | The data and time the procedure was started. |
| 42 | `PROC_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicated to type of procedure. 0 - Unknown 1 - encounter Procedure 2 - narrated procedure |
| 43 | `RANKING_CD` | DOUBLE | NOT NULL |  | Codified ranking description. The available codes are Primary and Secondary. |
| 44 | `REFERENCE_NBR` | VARCHAR(100) |  |  | The combination of the reference nbr and the contributor system code provides a unique identifier to the origin of the data. |
| 45 | `SEG_UNIQUE_KEY` | VARCHAR(100) |  |  | This field contains a unique identifier for one of the multiple repetitions of the HL7 segment. |
| 46 | `SUPPRESS_NARRATIVE_IND` | DOUBLE | NOT NULL |  | Indicator used to hide items from the historic procedure view. By default all of the existing data qualifies for history display. |
| 47 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | The service category history Id, or unique identifier, from the service category history table. It is an internal system assigned number. |
| 48 | `TISSUE_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for the tissue type. This is an optional field. An example would be moist or supple. |
| 49 | `UNITS_OF_SERVICE` | DOUBLE |  |  | A value representing the units of service for a procedure. (e.g. units of blood) |
| 50 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DIAG_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `MOD_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

## Referenced by (12)

| From table | Column |
|------------|--------|
| [DIAGNOSIS_PROCEDURE_RELTN](DIAGNOSIS_PROCEDURE_RELTN.md) | `PARENT_PROCEDURE_ID` |
| [PM_OFFER_PROC_RELTN](PM_OFFER_PROC_RELTN.md) | `PROCEDURE_ID` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `PROCEDURE_ID` |
| [PROCEDURE_ACTION](PROCEDURE_ACTION.md) | `PROCEDURE_ID` |
| [PROCEDURE_DIAGNOSIS_RELTN](PROCEDURE_DIAGNOSIS_RELTN.md) | `CHILD_PROCEDURE_ID` |
| [PROCEDURE_EXT_DATA](PROCEDURE_EXT_DATA.md) | `PROCEDURE_ID` |
| [PROCEDURE_HIST](PROCEDURE_HIST.md) | `PROCEDURE_ID` |
| [PROCEDURE_ORDER_RELTN](PROCEDURE_ORDER_RELTN.md) | `PROCEDURE_ID` |
| [PROCEDURE_PROCEDURE_RELTN](PROCEDURE_PROCEDURE_RELTN.md) | `CHILD_PROCEDURE_ID` |
| [PROCEDURE_PROCEDURE_RELTN](PROCEDURE_PROCEDURE_RELTN.md) | `PARENT_PROCEDURE_ID` |
| [PROCEDURE_SEC_LBL](PROCEDURE_SEC_LBL.md) | `PROCEDURE_ID` |
| [PROC_PRSNL_RELTN](PROC_PRSNL_RELTN.md) | `PROCEDURE_ID` |

