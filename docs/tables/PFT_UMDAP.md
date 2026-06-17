# PFT_UMDAP

> This table stores data related to UMDAP for California Mental Hospitals.

**Description:** ProFit Universal Method for Determining Ability to Pay  
**Table type:** ACTIVITY  
**Primary key:** `PFT_UMDAP_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Contains the UMDAP creation date. |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Contains the id of the person who created the UMDAP |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `INTERIM_IND` | DOUBLE |  |  | Identifies UMDAPs within the system as either annual or interim for data report reasons. |
| 10 | `NUM_OF_DEPENDENTS` | DOUBLE | NOT NULL |  | Number of Dependants related to the Guarantor. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 12 | `PFT_UMDAP_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 13 | `PREVIOUS_YEAR_REMAINING` | DOUBLE | NOT NULL |  | UMDAP Remaining amount from previous year. |
| 14 | `SIGNATURE_FILED_IND` | DOUBLE |  |  | Signature filed :0 - No, 1 - Yes |
| 15 | `TOTAL_AMT` | DOUBLE | NOT NULL |  | Total Amount totaled from questions. |
| 16 | `UMDAP_AMT_REMAINING` | DOUBLE | NOT NULL |  | Remaining amount for the year. |
| 17 | `UMDAP_YEARLY_TOTAL` | DOUBLE | NOT NULL |  | Total amount expected to by the guarantor. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_UMDAP_HIST](PFT_UMDAP_HIST.md) | `PFT_UMDAP_ID` |
| [PFT_UMDAP_QUESTION](PFT_UMDAP_QUESTION.md) | `PFT_UMDAP_ID` |

