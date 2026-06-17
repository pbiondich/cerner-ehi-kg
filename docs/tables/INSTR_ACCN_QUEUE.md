# INSTR_ACCN_QUEUE

> Queues accessions that are posted by an interfaced instrument.

**Description:** Instrument Accession Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) | NOT NULL |  | An accession uniquely identifies a specimen. |
| 2 | `IN_PROCESS_DT_TM` | DATETIME |  |  | The date and time that the user started working on the accession in a result entry conversation. Used to lock the record from another user. |
| 3 | `IN_PROCESS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User who has started working on the accession. Used to lock the accession for result entry conversation. |
| 4 | `PERF_DT_TM` | DATETIME |  |  | Date and time the record was written to the queue for review by result entry. |
| 5 | `QC_GROUP_ID` | DOUBLE | NOT NULL |  | If the accession resulted is QC, this is the ID of the group of results that were sent by the instrument. |
| 6 | `SEQUENCE` | DOUBLE | NOT NULL |  | Preserves the order in which accessions are posted for a specific service resource. |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The interfaced instrument that posted results for an accession. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IN_PROCESS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

