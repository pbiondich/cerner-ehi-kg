# PROV_DOC_PARTICIPANT

> Stores Participant information associated to the provenance document concept

**Description:** Provenance Document Participant  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `PARTICIPANT_ENTITY_ID` | DOUBLE | NOT NULL |  | Pk for a row in the participant table identified in field PARTICIPANT_ENTITY_NAME. |
| 4 | `PARTICIPANT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Participant table name e.g. PRSNL ORGANIZATION |
| 5 | `PARTICIPANT_ROLE_CD` | DOUBLE | NOT NULL |  | Code value describing the participant role in the provenance activity e.g. SOURCE INFORMANT. |
| 6 | `PARTICIPANT_TYPE_CD` | DOUBLE |  |  | The code identifies the type of participant to suppot patient writes. Examples are ORG PRSNL PATIENT RELATED-PESON |
| 7 | `PARTICIPATION_TYPE_CD` | DOUBLE | NOT NULL |  | How the participant contributed to the activity: Author or Transmitter. |
| 8 | `PROVENANCE_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | Pk for the Provenance_dOCUMENT table. |
| 9 | `PROV_DOC_PARTICIPANT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROVENANCE_DOCUMENT_ID` | [PROVENANCE_DOCUMENT](PROVENANCE_DOCUMENT.md) | `PROVENANCE_DOCUMENT_ID` |

