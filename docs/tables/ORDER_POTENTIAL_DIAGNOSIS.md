# ORDER_POTENTIAL_DIAGNOSIS

> Stores potential diagnosis information that is associated to an order.

**Description:** Order Potential Diagnosis  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSIS_DISPLAY` | VARCHAR(255) |  |  | The annotated display of the pending diagnosis displayed face up to the user |
| 2 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the nomenclature associated to this pending diagnosis after crossmapping occurred |
| 3 | `ORDER_POTENTIAL_DIAGNOSIS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the order_potential_diagnosis table. |
| 4 | `ORIGINATING_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the nomenclature associated to this pending diagnosis before crossmapping occurred |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORIGINATING_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

