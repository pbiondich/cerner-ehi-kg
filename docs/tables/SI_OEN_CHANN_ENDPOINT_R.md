# SI_OEN_CHANN_ENDPOINT_R

> This table is used to relate ComChannels to the Endpoints that it uses for communication for both source and destination

**Description:** Open engine ComChannel Endpoint Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RELATION_TYPE` | VARCHAR(31) | NOT NULL |  | Identifies whether the comchannel is using the endpoint as a source or destination for transaction data. |
| 2 | `SI_OEN_CHANN_ENDPOINT_R_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 3 | `SI_OEN_COMCHANNEL_ID` | DOUBLE | NOT NULL | FK→ | Id of the comchannel related to the endpoint |
| 4 | `SI_OEN_ENDPOINT_ID` | DOUBLE | NOT NULL | FK→ | Id of the endpoint related to the comchannel |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_OEN_COMCHANNEL_ID` | [SI_OEN_COMCHANNEL](SI_OEN_COMCHANNEL.md) | `SI_OEN_COMCHANNEL_ID` |
| `SI_OEN_ENDPOINT_ID` | [SI_OEN_ENDPOINT](SI_OEN_ENDPOINT.md) | `SI_OEN_ENDPOINT_ID` |

