# CYTO_SCREENING_EVENT

> This activity table contains parameters associated with the process of entering screening and rescreening results for cytology cases. Parameters such as the screener ID, screening date and time, adequacy flag, endocervical flag are included.

**Description:** Cytology Screening Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | This field indicates the event action (Initial screener, rescreener, or verifier). This field is currently not being used. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ADEQUACY_FLAG` | DOUBLE |  |  | This field contains a flag value documenting the microscopic evaluation of specimen adequacy assigned to the case at the time the screening event was written to the CYTO_SCREENING_EVENT table. |
| 4 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case information stored on the PATHOLOGY_CASE activity table. |
| 5 | `DIAGNOSTIC_CATEGORY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the diagnostic category assigned to the cytology case at the time the screening event was written to the CYTO_SCREENING_EVENT table. Diagnostic categories are stored on codeset 1314. |
| 6 | `ENDOCERV_IND` | DOUBLE |  |  | This field contains a flag value documenting the evaluation of collection technique (based on the presence/absence of endocervical cells) that was assigned to the case at the time the screening event was written to the CYTO_SCREENING_EVENT table. |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | This field is used in conjunction with the value stored in the VALID_FROM_DT_TM field to join to result information stored in OCF. |
| 8 | `INITIAL_SCREENER_IND` | DOUBLE |  |  | This field contains an indicator designating whether the screening event represents an initial screening activity (versus a rescreening activity). |
| 9 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the diagnosis alpha response (nomenclature) value assigned to the report at the time the screening event was written to the CYTO_SCREENING_EVENT table. |
| 10 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the table storing the reference range (alpha response values, in this example) information for the diagnosis alpha response report component. |
| 11 | `REVIEW_REASON_FLAG` | DOUBLE |  |  | This field contains a flag value documenting how a rescreening event was selected (user-specified versus system-specified). If the rescreening event was system-specified, the flag value also documents the reason the report was selected for rescreening. |
| 12 | `SCREENER_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the user who was the screener (or rescreener) for this screening event. This value could be used to join to personnel information on the PRSNL or PERSON tables. |
| 13 | `SCREEN_DT_TM` | DATETIME |  |  | This field contains the date and time the screening event occurred. |
| 14 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field documents the screening event sequence (for the same case). The initial screener's screening event would be sequenced first, and the first rescreener's screening event would be sequenced second, for example. |
| 15 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The service resource to which the case was assigned when the screening event was initiated. |
| 16 | `SPECIMEN_GROUPING_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 17 | `SPLIT_IND` | DOUBLE |  |  | This field is not used at this time. |
| 18 | `STANDARD_RPT_ID` | DOUBLE | NOT NULL | FK→ | This field is used to store the internal identification of the standard report (if any) used to enter report information for the case associated with the screening event. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VALID_FROM_DT_TM` | DATETIME |  |  | This field is used in conjunction with the value stored in the EVENT_ID field to join to result information stored in OCF. |
| 25 | `VERIFY_IND` | DOUBLE |  |  | This field contains a flag documenting whether or not the screening event record is associated with a perform result event or a verify result event. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `NOMENCLATURE_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `NOMENCLATURE_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `REFERENCE_RANGE_FACTOR_ID` |
| `STANDARD_RPT_ID` | [CYTO_STANDARD_RPT](CYTO_STANDARD_RPT.md) | `STANDARD_RPT_ID` |

