# INFUSION_CE_RELTN

> Stores all the cliincal events related to a particular infusion event.

**Description:** Infusion Clinical Event Relation  
**Table type:** ACTIVITY  
**Primary key:** `INFUSION_CE_RELTN_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | Date and time when the row became valid. |
| 3 | `CLINICAL_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The specific version of a clinical event that makes up a given infusion. |
| 4 | `CLINICAL_EVENT_SEQ` | DOUBLE | NOT NULL |  | Maintains the relative ordering of the clinical events associated to a given infusion event. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `INFUSION_BILLING_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the INFUSION_BILLING_EVENT table that holds the details about the infusion this clinical event is related to. |
| 7 | `INFUSION_CE_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the INFUSION_CE_RELTN table. |
| 8 | `PREV_INFUSION_CE_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The infusion clinical event relation id for the latest version of a given infusion record. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_EVENT_ID` | [CLINICAL_EVENT](CLINICAL_EVENT.md) | `CLINICAL_EVENT_ID` |
| `INFUSION_BILLING_EVENT_ID` | [INFUSION_BILLING_EVENT](INFUSION_BILLING_EVENT.md) | `INFUSION_BILLING_EVENT_ID` |
| `PREV_INFUSION_CE_RELTN_ID` | [INFUSION_CE_RELTN](INFUSION_CE_RELTN.md) | `INFUSION_CE_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INFUSION_CE_RELTN](INFUSION_CE_RELTN.md) | `PREV_INFUSION_CE_RELTN_ID` |

