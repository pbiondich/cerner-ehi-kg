# PBS_PRICING

> Australian Pharmaceutical Benefits Schedule - definition of pricing information

**Description:** PBS_PRICING  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BRAND_IDENT` | VARCHAR(45) |  |  | Brand XML Reference Identifier |
| 2 | `BRAND_PREMIUM` | DOUBLE | NOT NULL |  | Brand Premium Amt |
| 3 | `DISPENSED_COMMONWEALTH` | DOUBLE | NOT NULL |  | Commonwealth dispensed price |
| 4 | `DISPENSED_MANUFACTURER` | DOUBLE | NOT NULL |  | Manufacturer dispensed price |
| 5 | `DISPENSED_RETAIL` | DOUBLE | NOT NULL |  | Retail dispensed price |
| 6 | `DISPENSING_INCENTIVE` | DOUBLE | NOT NULL |  | Dispensing incentive price |
| 7 | `MAX_SAFETY_NET_VALUE` | DOUBLE | NOT NULL |  | Max_val_for_safety_net amt |
| 8 | `PBS_LISTING_ID` | DOUBLE | NOT NULL | FK→ | Foreign key PBS_LISTING |
| 9 | `PBS_PRICING_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the PBS_PRICING table. It is an internal system assigned number. |
| 10 | `PER_PACK_COMMONWEALTH` | DOUBLE | NOT NULL |  | Commonwealth price per pack |
| 11 | `PER_PACK_MANUFACTURER` | DOUBLE | NOT NULL |  | Manufacturer price per pack |
| 12 | `PER_PACK_REIMBURSEMENT` | DOUBLE | NOT NULL |  | Reimbursement price per pack |
| 13 | `PER_PACK_RETAIL` | DOUBLE | NOT NULL |  | Retail price per pack |
| 14 | `SPECIAL_PATIENT` | DOUBLE | NOT NULL |  | Special patient premium amt |
| 15 | `THERAPEUTIC_GROUP` | DOUBLE | NOT NULL |  | Therapeutic_group_premium amt |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PBS_LISTING_ID` | [PBS_LISTING](PBS_LISTING.md) | `PBS_LISTING_ID` |

