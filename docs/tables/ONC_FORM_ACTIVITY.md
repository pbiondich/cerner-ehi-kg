# ONC_FORM_ACTIVITY

> Stores activity data for oncology forms

**Description:** Oncology Forms Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOC_SET_REF_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the doc set that contains the reference data for the form |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | An EVENT_ID value from the CLINICAL_EVENT table |
| 4 | `FORM_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Identifier for a Onc_Form_Activity group. Identifies a logical Onc_Form_Activity row. There may be more than one row with the same Form_Activity_Id, but only one of those rows will be current as indicated by the Valid_Until_Dt_Tm field. THIS VALUE IS OBTAINED FROM A SEQUENCE AND WILL NOT EQUAL ANY PRIMARY KEY VALUE IN THE TABLE. |
| 5 | `FORM_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the results on the form |
| 6 | `ONC_DOCSETREF_CAT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from the ONC_DOCSETREF_CAT table |
| 7 | `ONC_FORM_ACTIVITY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the Onc_Form_Activity table. It is an internal system assigned number. |
| 8 | `ONSET_DT_TM` | DATETIME |  |  | The date and time selected for the onset of the problem. This field will be NULL if the onset date is documented along with the problem. |
| 9 | `ONSET_PRECISION_CD` | DOUBLE |  |  | Indicates to what precision the onset_dt_tm has been set. |
| 10 | `ONSET_PRECISION_FLAG` | DOUBLE |  |  | indicates to what level of accuracy the onset_dt_tm has been set. |
| 11 | `PERFORMED_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel id of provider who charted this form instance |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 13 | `PRE_RECURRENCE_FORM_ACT_ID` | DOUBLE | NOT NULL |  | The form_activity_id of the form that this entry is a recurrence of. |
| 14 | `PROBLEM_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the problem being related |
| 15 | `RECURRENCE_DT_TM` | DATETIME |  |  | Date of recurrence for cancer documented by the form |
| 16 | `RECURRENCE_PRECISION_CD` | DOUBLE |  |  | Indicates to what precision the recurrence_dt_tm has been set. |
| 17 | `RECURRENCE_PRECISION_FLAG` | DOUBLE |  |  | Indicates to what level of accuracy the recurrence_dt_tm has been set. |
| 18 | `TEXTUAL_RENDITION_EVENT_ID` | DOUBLE | NOT NULL |  | The event_id of the clinical note generated from the form data. (from CLINICAL_EVENT table) |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VALID_FROM_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 25 | `VALID_UNTIL_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 26 | `VERSION_DT_TM` | DATETIME |  |  | Date and time of the doc set reference that was documented. Used to pinpoint the correct version of the doc set that was used to document the results. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_REF_ID` | [DOC_SET_REF](DOC_SET_REF.md) | `DOC_SET_REF_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ONC_DOCSETREF_CAT_ID` | [ONC_DOCSETREF_CAT](ONC_DOCSETREF_CAT.md) | `ONC_DOCSETREF_CAT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | `PROBLEM_INSTANCE_ID` |

