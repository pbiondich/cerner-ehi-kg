# EXPEDITE_LOG

> This table is used by the Cpm Expedite server to log transactions so they can be reprocessed with debug logging enabled to determine how the server processed it.

**Description:** Troubleshooting table for the Cpm Expedite Server.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | This is the accession number from the request sent to the expedite server. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 3 | `EVENT_DT_TM` | DATETIME |  |  | This is the event date that was passed to the expedite server |
| 4 | `LOG_ID` | DOUBLE | NOT NULL |  | This is a unique id for the expedite_log table. |
| 5 | `MESSAGE` | LONGBLOB |  |  | This is the serialized transaction that is being logged. |
| 6 | `MESSAGE_SIZE` | DOUBLE |  |  | This is the size of the serialized transaction being logged. |
| 7 | `NEXT_LOG_ID` | DOUBLE | NOT NULL |  | If the size of the serialized message being logged is to large to fit in one record, it will be split into multiple records, and this points to the next record. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

