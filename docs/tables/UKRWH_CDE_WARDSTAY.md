# UKRWH_CDE_WARDSTAY

> Contains additional Ward stay level details relating to an Admitted Patient Care CDS Event.

**Description:** UK Reporting Warehouse Consolidated Data Extract Wardstay  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) |  |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `ENCNTR_SLICE_SK` | VARCHAR(40) |  |  | Identifies an Encounter as it relates to a time slice. |
| 4 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 10 | `LOC_NURSE_UNIT_REF` | VARCHAR(40) |  |  | This field is the patient location with a location type of nurse unit at the time the history row is written. |
| 11 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 12 | `UKRWH_CDE_WARDSTAY_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cde wardstay table. It is an internal system assigned number. |
| 13 | `UKRWH_CDS_APC_WARDSTAY_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds apc wardstay table. It is an internal system assigned number. |
| 14 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `WARD_STAY_END_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `WARD_STAY_SEQ` | DOUBLE |  |  | This is the value of the sequence of the ward stay within the CDS. |
| 21 | `WARD_STAY_START_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_APC_WARDSTAY_KEY` | [UKRWH_CDS_APC_WARDSTAY](UKRWH_CDS_APC_WARDSTAY.md) | `UKRWH_CDS_APC_WARDSTAY_KEY` |

