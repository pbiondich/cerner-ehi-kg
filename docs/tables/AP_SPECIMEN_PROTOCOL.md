# AP_SPECIMEN_PROTOCOL

> This reference table contains the optional default processing task protocols that can be established for a specific specimen, pathologist, and/or case prefix.

**Description:** AP Specimen Protocol  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PATHOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | If the processing protocol is associated with a pathologist, this field contains the user's internal ID value. This value could be used to join to personnel information on the PRSNL or PERSON tables. |
| 2 | `PREFIX_ID` | DOUBLE | NOT NULL |  | If the processing protocol is associated with a case prefix value, this field contains the internal ID associated with the prefix. This foreign key value could be used to join to prefix information included on the AP_PREFIX reference table. |
| 3 | `PROTOCOL_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies the row (the protocol) included on the AP_SPECIMEN_PROTOCOL table. |
| 4 | `SPECIMEN_CD` | DOUBLE | NOT NULL |  | If the processing protocol is associated with a specimen, this field contains the specimen's internal ID value. This value could be used to join to specimen information stored in codeset 1306. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

