# AP_QA_INFO

> This activity table contains the quality assurance indicators associated with gynecologic cytology cases. Indicators include classifications such as normal, atypical, abnormal, and unsatisfactory.

**Description:** AP Quality Assurance Info  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVATED_DT_TM` | DATETIME |  |  | This field contains the date and time the record was written to the AP_QA_INFO table. |
| 2 | `ACTIVATED_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the user who performed the activation event associated with the QA record. The activation event is most often the report verification event. This ID could be used to join to the user tables. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `CANCEL_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 5 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case information stored on the PATHOLOGY_CASE activity table. |
| 6 | `COMPLETE_DT_TM` | DATETIME |  |  | This field is not used at this time. |
| 7 | `COMPLETE_ID` | DOUBLE | NOT NULL | FK→ | This field is not used at this time. |
| 8 | `FLAG_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains a reference to codeset 1316 indicating the type of quality assurance that is associated with this entry. Quality assurance flag options include previous normal, previous atypical, previous abnormal, and clinical high risk. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `QA_FLAG_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies the row (the quality assurance flag) included on the AP_QA_INFO table. |
| 11 | `SUSPEND_DT_TM` | DATETIME |  |  | This field is not used at this time. |
| 12 | `SUSPEND_ID` | DOUBLE | NOT NULL | FK→ | This field is not used at this time. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVATED_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `COMPLETE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SUSPEND_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

