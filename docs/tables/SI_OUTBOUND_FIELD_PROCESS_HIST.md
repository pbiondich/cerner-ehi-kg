# SI_OUTBOUND_FIELD_PROCESS_HIST

> This table contains records related to the Outbound Field Processing table.

**Description:** System Integration Outbound Field Processing History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FIELD_PROCESSING_CD` | DOUBLE | NOT NULL |  | This field defines the processing method for the specified processing type. |
| 6 | `FIELD_PROCESSING_CS` | DOUBLE | NOT NULL |  | This field defines the code_set for the processing method for the specified processing type. |
| 7 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made new modification on the Outbound_Field_Processing table |
| 8 | `NULL_STRING` | VARCHAR(200) |  |  | This defines a string attribute associated with the process type. |
| 9 | `ORIG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made original modification on the Outbound_Field_Processing table |
| 10 | `PROCESS_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Define the processing type entity. |
| 11 | `REC_BEG_EFF_DT_TM` | DATETIME |  |  | Copy of the Beg_Eff_Dt_TM from the Outbound_Field_Processing Table |
| 12 | `SEQ_NUM` | DOUBLE | NOT NULL |  | Defines the sequence number of the related outbound field processin the table. |
| 13 | `SI_OUTBOUND_FIELD_PRCS_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key column |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SYSTEM_CD` | [OUTBOUND_FIELD_PROCESSING](OUTBOUND_FIELD_PROCESSING.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PROCESS_TYPE_CD` | [OUTBOUND_FIELD_PROCESSING](OUTBOUND_FIELD_PROCESSING.md) | `PROCESS_TYPE_CD` |

